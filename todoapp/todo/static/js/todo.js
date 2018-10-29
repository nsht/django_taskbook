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


    // New Todo Modal Functions
    $('#new_todo_link').click(function(event){
        event.preventDefault();
        $('.modal').addClass('is-active');
        $('#id_todo_item').val('');
        $('#id_todo_item').focus();
    });

    $('.modal-background').click(function(){
       $('.modal').removeClass('is-active');
    });

    $('.modal-close').click(function(){
        $('.modal').removeClass('is-active');
     });

// New Todo form submit functions
    $('#new_todo_form').submit(function(event){
        event.preventDefault();
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
        var data = {
            csrfmiddlewaretoken: csrftoken,
            todo_item:$('#id_todo_item').val()
        }
        console.log(data);
        $.post("/add",data).done(function( result ) {
            $('.modal').removeClass('is-active');
        })
        .done(function(result){
            console.log(result)
            html = $.parseHTML(result)
            $('#parent_list').append(result)

        });
    });




});

// Tried to use plain js instead of jquery
document.onkeyup = function(e) {
    if(e.which == 78){
        if(!document.getElementById('new_todo_modal').classList.contains("is-active")) {
            document.getElementById('new_todo_modal').classList.add("is-active");
            document.getElementById('id_todo_item').value = "";
            document.getElementById('id_todo_item').focus();
        }
    }
    else if(e.which == 27){
        if(document.getElementById('new_todo_modal').classList.contains("is-active")) {
            document.getElementById('new_todo_modal').classList.remove("is-active");
        }
    }

}
