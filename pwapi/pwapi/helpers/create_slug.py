import re
import uuid
from . db import find_single_instance

def create_slug(text, slug, model, id):
    # How to deal with non unique
    if slug == "" or slug == None:
        slug = text
    sanitized_slug = sanitize_for_url(slug)
    dup_instance = find_single_instance(model, "slug", sanitized_slug)
    if dup_instance:
        if id != dup_instance.id:
          sanitized_slug += "-" + str(uuid.uuid4())
          sanitized_slug = sanitize_for_url(sanitized_slug)
    return sanitized_slug
  
def sanitize_for_url(slug):
    sanitized_slug = re.sub(r"[\W_]", "-", slug)
    sanitized_slug = re.sub(r"--", "-", sanitized_slug).lower()
    if sanitized_slug.endswith("-"):
      sanitized_slug = sanitized_slug[:-1]
    print("SLUG:", sanitized_slug)
    if "--" in sanitized_slug:
        return sanitize_for_url(sanitized_slug)
    return sanitized_slug
