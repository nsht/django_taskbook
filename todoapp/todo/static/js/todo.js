$(document).ready(function(){
    $('.completed-checkbox').click(function(){
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
        var data = {
            csrfmiddlewaretoken: csrftoken,
            id:$(this).attr('name')
        }

        if($(this).hasClass('subitem-checkbox')){
            data['type'] = 'subitem';
        }
        else{
            data['type'] = 'todoitem';
        }

        if($(this).parent().hasClass('task-completed')){
            $(this).parent().removeClass('task-completed')
        }
        else{
            $(this).parent().addClass('task-completed')
        }
        $.post("/toggle-completion",data).done(function( result ) {
        });

    });

    $('.star-toggle').click(function(){
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
        var data = {
            csrfmiddlewaretoken: csrftoken,
            id:$(this).attr('id')
        }

        if($(this).hasClass('has-text-warning')){
            $(this).removeClass('has-text-warning')
            $(this).addClass('has-text-grey')

        }
        else{
            $(this).removeClass('has-text-grey')
            $(this).addClass('has-text-warning')

        }
        $.post("/toggle-star",data).done(function( result ) {
        });


    });
});