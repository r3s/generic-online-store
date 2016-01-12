function delete_item(id){
  $('#data-placeholder').html(id);
  $('#confirm-modal').modal();
}
function delete_confirmed(){
  var id = $('#data-placeholder').html();
  $('#confirm-modal').modal('hide');
  delete_request(id);
}
function delete_cancel(){
  $('#data-placeholder').html("");
}
function ajax_request(url,method,data,callback,param){
    $.ajax({
        type:method,
        url:url,
        data: data,
        success: function(json_obj){
            if (json_obj['status']=="success"){
              callback(param);
            }
        }
    });
}
function destroy_row(id){
  $(id).fadeToggle();
}
function delete_request(id){
  var url = $('#data-delete-url').html();
  url = url.replace('0', id);
  ajax_request(url,"GET","", destroy_row,"#row_"+id);
}
