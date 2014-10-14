$(function()    {
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    $('table').on('click', 'td', function(e) {
        var old_data = $(this).val();
        var t = e.target || e.srcElement;
        var elm_name = t.tagName.toLowerCase();
        if(elm_name == 'input') {return false;}
        var old_data = $(this).html();
        var _id = $(this).attr('id');
        var code = '<input type="text" id=" ' + _id + ' " value="' + old_data + '" />';
        $(this).empty().append(code);
        $("#" + _id).focus();
        $(document).on('blur', "#" + _id, function(e) {
            var value = e.target.value;
            if (old_data == value) {
                return;
            }
            var data = {
                'old_data': old_data,
                'new_data': value
            }
            $.ajax({
                type: 'POST',
                url: '/change/' + parseInt(_id, 10) + '/',
                data: data,
                headers: {'X-CSRFToken': csrftoken},
                success: changeSuccess,
                datatype:'html'
            });
            function changeSuccess(data, textStatus, jqXHR){
                $(this).parent().empty().html(data);
            }
        });
    });
}); 
