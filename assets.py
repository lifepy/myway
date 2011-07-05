from django_assets import Bundle, register

jquery = Bundle('jquery/jquery-1.5.min.js', filters='jsmin', output='assets/js/jquery.js')
register('jquery',jquery)

jquery_autocomplete = Bundle(
    Bundle('jquery/autocomplete/jquery.autocomplete.js', 'jquery/autocomplete/lib/jquery.bgiframe.min.js', filters='jsmin', output='assets/js/jquery.autocomplete.js'),
    Bundle('jquery/autocomplete/jquery.autocomplete.css', filters='cssutils', output='assets/css/jquery.autocomplete.css'),
)
register('autocomplete',jquery_autocomplete)
