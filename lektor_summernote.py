import email

import pkg_resources
from flask import Blueprint, render_template_string
from lektor.admin.modules import dash
from lektor.pluginsystem import Plugin


TEMPLATE = '''
{% extends "dash.html" %}
{% block scripts %}
  {{ super() }}

<script src="https://cdn.jsdelivr.net/npm/jquery@3.4.1/dist/jquery.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>

<script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.js"></script>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote-bs4.min.css" rel="stylesheet">


<link rel="stylesheet" type="text/css" href="/admin/static/gen/vendor.css">
<link rel="stylesheet" type="text/css" href="/admin/static/gen/styles.css">

<script>
//Refreshes the page when the top level, side sublevel or search links are clicked
document.addEventListener("click", (e) => {
  const topNode = e.target.closest('li.record-crumb');
  const sideNode = e.target.closest('ul.nav.record-children');
  const search = e.target.closest('ul.search-results');
  if (topNode || sideNode || search) {
    location.reload();
    load();
  }
})
//Refreshes the page if the user click one of the browser functions such as 'back'
window.addEventListener('popstate', function () {
  const [entry] = performance.getEntriesByType("navigation");
  if (entry["type"] === "reload" || entry["entryType"] === "navigation") {
    location.reload();
    load();
  }
});
//Loads the page when changes are made
function load() {
  document.addEventListener("DOMContentLoaded", function () {
    let stateCheck = setInterval(() => {
      if (document.readyState === 'complete') {
        clearInterval(stateCheck);
      }
    }, 500);
  });
}
//Loads the functions
load();
</script>
<script>
//Summernote function
(new MutationObserver(function () {
    [...document.getElementsByTagName('textarea')].forEach(e => {
        if (e.className === 'form-control') {
            e.id = "summernote";
            $('#summernote').summernote({
                dialogsInBody: true,
                height: 800,   //set editable area's height
                toolbar: [
                    ['style', ['style']],
                    ['font', ['bold', 'italic', 'underline', 'clear']],
                    ['fontname', ['fontname']],
                    ['fontsize', ['fontsize']],
                    ['color', ['color']],
                    ['para', ['ul', 'ol', 'paragraph']],
                    ['height', ['height']],
                    ['help', ['help']],
                    ['insert', ['link', 'picture', 'video']],
                    ['table', ['table']],
                    ['misc', ['undo', 'redo', 'fullscreen', 'codeview']],
                ],
                popover: {
                    image: [
                        ['image', ['resizeFull', 'resizeHalf', 'resizeQuarter', 'resizeNone']],
                        ['float', ['floatLeft', 'floatRight', 'floatNone']],
                        ['remove', ['removeMedia']]
                    ],
                    link: [
                        ['link', ['linkDialogShow', 'unlink']]
                    ],
                    table: [
                        ['add', ['addRowDown', 'addRowUp', 'addColLeft', 'addColRight']],
                        ['delete', ['deleteRow', 'deleteCol', 'deleteTable']],
                    ],
                },
                callbacks: {
                    onChange: function (contents, $editable) {
                        const nativeTextAreaValueSetter = Object.getOwnPropertyDescriptor(window.HTMLTextAreaElement.prototype, 'value').set;
                        nativeTextAreaValueSetter.call(e, contents);
                        const inputEvent = new Event('input', { bubbles: true });
                        inputEvent.simulated = true;
                        e.dispatchEvent(inputEvent);
                    },
                    onBlurCodeview: function () {
                        let codeviewHtml = $(this).siblings('div.note-editor').find('.note-codable').val();
                        $(e).val(codeviewHtml);
                    }
                }
            })
        };
    });
})).observe(
    document.getElementsByTagName('body')[0],
    {
        subtree: true,
        childList: true
    },
);

  </script>
  
{% endblock %}
'''


def get_description(mod):
    distribution = pkg_resources.get_distribution(mod)
    if distribution.has_metadata('PKG-INFO'):
        meta = distribution.get_metadata('PKG-INFO')
    elif distribution.has_metadata('METADATA'):
        meta = distribution.get_metadata('METADATA')
    else:
        return None
    return email.message_from_string(meta).get('Summary', None)

def patched_endpoint(*args, **kwargs):
    return render_template_string(TEMPLATE)

class SummernotePlugin(Plugin):
    name = 'Summernote'
    description = get_description(__module__)
    def on_server_spawn(self, *args, **kwargs):
        # remove all rules except the first one which is edit redirect
        while len(dash.bp.deferred_functions) > 1:
            dash.bp.deferred_functions.pop()
        # fill all the rules back with the wrapper template
        for path, endpoint in dash.endpoints:
            dash.bp.add_url_rule(path, endpoint, patched_endpoint)
