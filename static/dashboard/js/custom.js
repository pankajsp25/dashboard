/**
 *
 * You can write your JS code here, DO NOT touch the default style file
 * because it will make it harder for you to update.
 * 
 */

"use strict";

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

var get_danger_alert = function(msg) {

 var error_html = `
 <div class="alert alert-danger alert-dismissible show fade">
    <div class="alert-body">
      <button class="close" data-dismiss="alert">
        <span>×</span>
      </button>`+
      msg
    +`</div>
  </div>
 `;

  return error_html;
}

var get_success_alert = function(msg) {
var html = `
  <div class="alert alert-success alert-dismissible show fade">
      <div class="alert-body">
        <button class="close" data-dismiss="alert">
        <span>×</span>
        </button>`+
          msg
        +`</div>
   </div>
`;

return html
}

function bind_data(obj) {
  for (var key in obj) {
    if (obj.hasOwnProperty(key)) {
      var val = obj[key];
      $('.data-'+key).html(val)
    }
  }
}

var submit_form_ajax = function(obj) {
$('#'+obj.form).submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: obj.method,
            dataType: "json",
            url: obj.url, // the file to call
            beforeSend: function (xhr) {
              xhr.setRequestHeader ("X-CSRFToken", csrftoken);
            },
            success: function(response) { // on success..

                 bind_data(response)
                 $('.data-full-name').html(response.first_name + ' ' + response.last_name)
                 $("#"+obj.result_div).html(get_success_alert(obj.success_msg)); // update the DIV
            },
            error: function(data) {
             var error_msg = JSON.stringify(data)
             var error_obj = JSON.parse(error_msg).responseJSON
             for (var key in error_obj) {
                if (error_obj.hasOwnProperty(key)) {
                  var val = error_obj[key];

                  $("#"+obj.result_div).append(get_danger_alert(val))
                  console.log(val);
                }
             }
        }
        });
        return false;
    });
}
