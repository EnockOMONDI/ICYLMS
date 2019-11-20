import json
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings


def landpageprod_page(request):
    return render(request, 'productionpages/page/index2.html',{
        'tab': 'productionpages',
        'local_css_urls': [                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ],
        'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js2/plugins/moment.min.js ",
                           "js2/plugins/bootstrap-datetimepicker.js",
                           "js2/plugins/nouislider.min.js", 
                           "js2/plugins/jquery.sharrre.js", 
                           "js2/plugins/bootstrap-tagsinput.js",            
                           "js2/plugins/bootstrap-selectpicker.js",                         
                           "js2/plugins/jasny-bootstrap.min.js",
                           "js2/plugins/jquery.flexisel.js",
                           "js2/modernizr.js",
                           "js2/vertical-nav.js",
                           "js2/buttons.js",
                           "js2/demo.js",
                           "js2/material-kit.min1036.js?v=2.1.1" ],
    })

def graduants_page(request):
    return render(request, 'productionpages/page/graduants.html',{
        'tab': 'graduantspage',
        'local_css_urls': [                    
                            "css2/demo.css",
                             "css2/material-kit.min1036.css",   
                            "css2/vertical-nav.css"
                            ],
        'local_js_urls': [ "core/jquery.min.js",
                           "core/popper.min.js",
                           "core/bootstrap-material-design.min.js",
                           "js2/plugins/moment.min.js ",
                           "js2/plugins/bootstrap-datetimepicker.js",
                           "js2/plugins/nouislider.min.js", 
                           "js2/plugins/jquery.sharrre.js", 
                           "js2/plugins/bootstrap-tagsinput.js",            
                           "js2/plugins/bootstrap-selectpicker.js",                         
                           "js2/plugins/jasny-bootstrap.min.js",
                           "js2/plugins/jquery.flexisel.js",
                           "js2/modernizr.js",
                           "js2/vertical-nav.js",
                           "js2/buttons.js",
                           "js2/demo.js",
                           "js2/material-kit.min1036.js?v=2.1.1" ],
    })


