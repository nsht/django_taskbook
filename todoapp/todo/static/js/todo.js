$(document).ready(function(){

    // Check and uncheck TodoItems
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

    // Star and Unstar TodoItems
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

    $('#new_todo_link').click(function(event){
        event.preventDefault();
        $('.modal').addClass('is-active');
    });

    $('.modal-background').click(function(){
       $('.modal').removeClass('is-active');
    });

    $('.modal-close').click(function(){
        $('.modal').removeClass('is-active');
     });

});