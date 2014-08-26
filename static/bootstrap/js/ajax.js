$(function()    {
    $('td').click(function(e)   {
        var old_data = $(this).val();
        var t = e.target || e.srcElement;
        var elm_name = t.tagName.toLowerCase();
        if(elm_name == 'input') {return false;}
        var new_data = $(this).html();
        var _id = $(this).attr('id');
        var code = '<input type="text" id=" '+_id+' " value="'+new_data+'" />';
        $(this).empty().append(code);
        $("#" + "_id").focus();
        $("#" + "_id").blur(function(){
            $.ajax({
                type: "POST",
                url: "/change/",
                data:{
                    'old_data':old_data,
                    'new_data':new_data,
                    '_id':_id,
                    'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
                    },
                success: changeSuccess,
                datatype:'html'
            });
            function changeSuccess(data, textStatus, jqXHR){
                $(this).parent().empty().html(data);
            }
        });
    });
}); 