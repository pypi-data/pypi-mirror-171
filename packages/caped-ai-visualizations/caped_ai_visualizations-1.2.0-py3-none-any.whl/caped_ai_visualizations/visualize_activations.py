import os
from oneat.NEATModels.loss import volume_yolo_loss, static_yolo_loss, dynamic_yolo_loss
from oneat.NEATModels.neat_vollnet import NEATVollNet, CreateVolume
from oneat.NEATModels.neat_lstm import NEATLRNet

from oneat.NEATModels.neat_dynamic_resnet import NEATTResNet
from oneat.NEATModels.neat_static_resnet import NEATResNet
from vollseg import CARE, UNET, StarDist2D, StarDist3D, MASKUNET
import numpy as np
from oneat.NEATUtils.utils import load_json, normalizeFloatZeroOne
from keras import models 
from keras.models import load_model
from tifffile import imread
from oneat.NEATModels.nets import Concat
import tensorflow as tf
import napari
from .visualize_action_volume_boxes import VisualizeBoxes
class visualize_activations(object):
    
    def __init__(self,  catconfig: dict, cordconfig: dict, model_dir: str,  imagename: str, model_name = None,
                 segdir = None, visualize_point = None, oneat_vollnet = False, start_project_mid = 4, end_project_mid = 1,
                 oneat_lrnet = False, oneat_tresnet = False, oneat_resnet = False, voll_starnet_2D = False,
                 voll_starnet_3D = False, voll_unet = False, voll_care = False, layer_viz_start = None,
                 event_threshold = 0.9, event_confidence = 0.9, nms_function = 'iou',
                 layer_viz_end = None, dtype = np.uint8, n_tiles = (1,1,1), normalize = True):
        
        self.viewer = napari.Viewer()
        self.model_dir = model_dir 
        self.imagename = imagename 
        self.model_name = model_name
        self.segdir = segdir
        self.start_project_mid = start_project_mid
        self.end_project_mid = end_project_mid
        self.event_threshold = event_threshold 
        self.event_confidence = event_confidence
        self.nms_function = nms_function  
        self.oneat_vollnet = oneat_vollnet 
        self.oneat_lrnet = oneat_lrnet 
        self.oneat_tresnet = oneat_tresnet 
        self.oneat_resnet = oneat_resnet
        self.voll_starnet_2D = voll_starnet_2D 
        self.voll_starnet_3D = voll_starnet_3D
        self.voll_unet = voll_unet 
        self.voll_care = voll_care 
        self.catconfig = catconfig 
        self.cordconfig = cordconfig 
        self.layer_viz_start = layer_viz_start
        self.layer_viz_end  = layer_viz_end 
        self.dtype = dtype 
        self.n_tiles = n_tiles 
        self.normalize = normalize
        self.key_cord = self.cordconfig
        self.categories = len(self.catconfig)
        self.key_categories = self.catconfig
        self.image = imread(imagename).astype(self.dtype)
        self.visualize_point = visualize_point
        self.all_max_activations = {}
        if self.oneat_vollnet or self.oneat_lrnet or self.oneat_tresnet or self.oneat_resnet: 
                self.config = load_json(os.path.join(self.model_dir, 'parameters.json'))
                
                self.box_vector = self.config['box_vector']
                self.show = self.config['show']
                
                self.depth = self.config['depth']
                self.start_kernel = self.config['start_kernel']
                self.mid_kernel = self.config['mid_kernel']
                self.learning_rate = self.config['learning_rate']
                self.epochs = self.config['epochs']
                self.startfilter = self.config['startfilter']
                self.batch_size = self.config['batch_size']
                self.multievent = self.config['multievent']
                self.imagex = self.config['imagex']
                self.imagey = self.config['imagey']
                self.imagez = self.config['imagez']
                self.imaget = self.config['size_tminus'] + self.config['size_tplus'] + 1
                self.size_tminus = self.config['size_tminus']
                self.size_tplus = self.config['size_tplus']
                self.nboxes = self.config['nboxes']
                self.stage_number = self.config['stage_number']
                self.last_conv_factor = 2 ** (self.stage_number - 1)
                self.gridx = 1
                self.gridy = 1
                self.gridz = 1
                self.yolo_v0 = self.config['yolo_v0']
                self.yolo_v1 = self.config['yolo_v1']
                self.yolo_v2 = self.config['yolo_v2']
                self.stride = self.config['stride']
                if self.multievent == True:
                        self.entropy = 'binary'

                if self.multievent == False:
                    self.entropy = 'notbinary' 
        
    def _load_model_loss(self):
        
        
        self.viewer.add_image(self.image.astype('float32'), name= 'Image', blending= 'additive' )
        
        if self.normalize: 
            self.image = normalizeFloatZeroOne(self.image, 1, 99.8, dtype = self.dtype)
        self.image = np.expand_dims(self.image, 0)    
            
        if self.oneat_vollnet: 
            
            self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1])  
            self.yololoss = volume_yolo_loss(self.categories, self.gridx, self.gridy, self.gridz, self.nboxes,
                                            self.box_vector, self.entropy)
            self.model = NEATVollNet(None, self.model_dir, self.catconfig, self.cordconfig)
            marker_tree =  self.model.get_markers(self.imagename, self.segdir)
            self.model.predict(self.imagename,
                           n_tiles = self.n_tiles, 
                           event_threshold = self.event_threshold, 
                           event_confidence = self.event_confidence,
                           marker_tree = marker_tree, 
                           nms_function = self.nms_function,
                           normalize = self.normalize, 
                           activations = True)
        
        if self.oneat_tresnet:
            self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1]) 
            self.yololoss = static_yolo_loss(self.categories, self.gridx, self.gridy, self.nboxes, self.box_vector,
                                                        self.entropy)
            self.model = NEATTResNet(None, self.model_dir, self.catconfig, self.cordconfig)
            marker_tree = self.model.get_markers( self.imagename, 
                                                  self.segdir, 
                                                  start_project_mid = self.start_project_mid,
                                                  end_project_mid = self.end_project_mid)
            self.model.predict(self.imagename,
                                n_tiles = self.n_tiles,
                                event_threshold = self.event_threshold,
                                event_confidence = self.event_confidence,
                                marker_tree = marker_tree,
                                nms_function = self.nms_function,
                                stert_project_mid = self.start_project_mid,
                                end_project_mid = self.end_project_mid,
                                normalze = self.normalize, 
                                activations = True)
        
        if self.oneat_lrnet:
            self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1]) 
            self.yololoss = dynamic_yolo_loss(self.categories, self.gridx, self.gridy, 1, self.nboxes,
                                          self.box_vector, self.entropy)
            self.model = NEATLRNet(None, self.model_dir,self.catconfig, self.cordconfig)
            marker_tree =  self.model.get_markers(self.imagename, 
                                                self.segdir,
                                                start_project_mid = self.start_project_mid,
                                                end_project_mid = self.end_project_mid,  
                                                ) 
            self.model.predict(self.imagename,
                               n_tiles = self.n_tiles,
                               event_threshold = self.event_threshold,
                               event_confidence = self.event_confidence,
                               marker_tree = marker_tree,
                               nms_function = self.nms_function,
                               start_project_mid = self.start_project_mid,
                               end_project_mid = self.end_project_mid,
                               normalize = self.normalize, 
                               activations = True)

        if self.oneat_resnet:
            self.pad_width = (self.image.shape[-2], self.image.shape[-1]) 
            self.yololoss = static_yolo_loss(self.categories, self.gridx, self.gridy, self.nboxes, self.box_vector,
                                                        self.entropy)
            self.model = NEATResNet(None, self.model_dir ,  self.catconfig, self.cordconfig)
            self.model.predict(self.imagename,
                               event_threshold = self.event_threshold,
                               event_confidence = self.event_confidence,
                               n_tiles = self.n_tiles, 
                               activations = True
                               )
     
        elif self.voll_starnet_2D:
                if len(self.image.shape) == 4:
                    self.image = self.image[0,0,:,:]
                if len(self.image.shape) == 3:
                    self.image = self.image[0,:,:]     
                self.pad_width = (self.image.shape[-2], self.image.shape[-1]) 
                self.model =  StarDist2D(None, name=self.model_name, basedir=self.model_dir)
                self.prediction_star = self.model.predict(self.image)         
        elif self.voll_starnet_3D:
                if len(self.image.shape) == 4:
                    self.image = self.image[0,:,:,:]
                self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1]) 
                self.model =  StarDist3D(None, name=self.model_name, basedir=self.model_dir)
                self.prediction_star = self.model.predict(self.image)     
        elif self.voll_unet:
                if len(self.image.shape) == 4:
                    self.image = self.image[0,:,:,:]
                if len(self.image.shape) >=3:
                     self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1]) 
                else:
                     self.pad_width = (self.image.shape[-2], self.image.shape[-1])      
                self.model =  UNET(None, name=self.model_name, basedir=self.model_dir)  
                self.prediction_unet = self.model.predict(self.image)
        elif self.voll_care:
                if len(self.image.shape) == 4:
                    self.image = self.image[0,:,:,:]
                if len(self.image.shape) >=3:
                     self.pad_width = (self.image.shape[-3], self.image.shape[-2], self.image.shape[-1]) 
                else:
                     self.pad_width = (self.image.shape[-2], self.image.shape[-1])
                self.model =  CARE(None, name=self.model_name, basedir=self.model_dir)
                self.prediction_care = self.model.predict(self.image)
                
                
    def _draw_boxes(self):    
        
        viz_box = VisualizeBoxes(viewer = self.viewer, key_categories = self.key_categories, event_threshold = self.event_threshold)
        
        if self.oneat_vollnet:
             
             viz_box.create_volume_boxes(iou_classedboxes = self.model.all_iou_classedboxes)
             
        if self.oneat_lrnet:
            
            viz_box.create_volume_boxes(iou_classedboxes = self.model.all_iou_classedboxes, volumetric = False, shape = self.model.image.shape)
            
        if self.oneat_tresnet:
            
            viz_box.create_volume_boxes(iou_classedboxes = self.model.all_iou_classedboxes, volumetric = False, shape = self.model.image.shape)
            
        if self.oneat_resnet:
            
            viz_box.create_area_boxes(iou_classedboxes = self.model.all_iou_classedboxes)           
              
                
                
    def _activations_predictions(self):
         
                
        self.model = self.model._build()  
        
        self.max_activation_layer = len(self.model.layers)
        if self.layer_viz_start is None:
            self.layer_viz_start = 0 
        if self.layer_viz_end is None:
            self.layer_viz_end = self.max_activation_layer
        
        if self.visualize_point is not None:
            if self.visualize_point < self.size_tminus:
                self.visualize_point = self.size_tminus + 1
                
                
            smallimage = CreateVolume(self.image, self.size_tminus, self.size_tplus, self.visualize_point)
            layer_outputs = [layer.output for layer in self.model.layers[self.layer_viz_start:self.layer_viz_end]]
            self.activation_model = models.Model(inputs = self.model.input, outputs=layer_outputs)   
            smallimage = np.expand_dims(smallimage,0) 
            if self.oneat_vollnet:
                
                smallimage = np.reshape(smallimage, (smallimage.shape[0], smallimage.shape[2], smallimage.shape[3],smallimage.shape[4], smallimage.shape[1]))
            
            self.activations = self.activation_model.predict(smallimage)
            self.all_max_activations[self.visualize_point] = self.activations
           
    def VizualizeActivations(self):    
        print('loading model and losses, running prediction')
        self._load_model_loss()
        print('prediction done, creating boxes')
        self._draw_boxes()
        print('boxes done, creating activation maps')
        self._activations_predictions()
        
        
        
        for (k,v) in self.all_max_activations.items():
            time = k
            activations = v
            for count, activation in enumerate(activations):
                max_activation = np.sum(activation, axis = -1)
                max_activation = normalizeFloatZeroOne(max_activation, 1, 99.8, dtype = self.dtype)   
                print('adding activations to Napari')          
                self.viewer.add_image(max_activation.astype('float32'), name= 'Activation_count' + str(count) + 'time_' + str(time), blending= 'additive', colormap='inferno' )
        napari.run()