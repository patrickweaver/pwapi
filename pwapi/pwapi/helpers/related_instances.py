from django.forms.models import model_to_dict

from django.http import JsonResponse

from . general import get_model_name, validate_body
from . responses import error
from . db import find_single_instance, save_object_instance

def add_child_to(request, parent_model, child_model, parent_key, parent_identifier_value):
  
    def get_modify_with(parent_instance, child_model_name):
      return getattr(parent_instance, child_model_name).add
    
    return modify_child_on(request, parent_model, child_model, parent_key, parent_identifier_value, get_modify_with)
  
  
def remove_child_from(request, parent_model, child_model, parent_key, parent_identifier_value):
  
    def get_modify_with(parent_instance, child_model_name):
      return getattr(parent_instance, child_model_name).remove
    
    return modify_child_on(request, parent_model, child_model, parent_key, parent_identifier_value, get_modify_with)
    
    
def modify_child_on(request, parent_model, child_model, parent_key, parent_identifier_value, get_modify_with):
    child_model_name = get_model_name(child_model)
    parsed_body = validate_body(request)
            
    parent_instance = find_single_instance(parent_model, parent_key, parent_identifier_value)
    if not parent_instance:
        return error(parent_model__name__ + " not found")
      
    try:
        child_identifier = parsed_body["identifier"]
        child_identifier_value = parsed_body["value"]
    except:
        return error('No identifier provided')

    try:
        child_instance = find_single_instance(child_model, child_identifier, child_identifier_value)
        modify_with = get_modify_with(parent_instance, child_model_name)
        modify_with(child_instance)
    except:
        print(sys.exc_info())
        return error('Error adding or removing child')
    
    # Should generalize this:
    updated_parent_instance_dict = model_to_dict(parent_instance)
    if not updated_parent_instance_dict:
        return error('Error generating response')
    children_dicts = []
    for child in updated_parent_instance_dict[child_model_name]:
        children_dicts.append(model_to_dict(child))
    updated_parent_instance_dict[child_model_name] = children_dicts
    updated_parent_instance_dict['success'] = True
    return JsonResponse(updated_parent_instance_dict, safe=False)