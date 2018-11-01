// TODO need to refactor messy code and hacks

$(document).ready(function(){
    // Check and uncheck TodoItems
    onclick_bind()
    function onclick_bind(){
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
            id:$(this).attr('data-todoid')
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
    }

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
            var aclick = document.getElementsByClassName('new-sub-item');

            Array.from(aclick).forEach(function(element) {
                element.addEventListener("click", handleClick,false);
              });
              onclick_bind()

        });
    });

    $(document).keypress(function(e) {

        if(e.which == 13) {
            if ($('.new-todo-text-box').is(":focus")){
                var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
                var data = {
                    csrfmiddlewaretoken: csrftoken,
                    todo_item_id:$('.new-todo-text-box').attr('data-todoid'),
                    sub_item:$('.new-todo-text-box').val()
                }
                todo_item_id = $('.new-todo-text-box').attr('data-todoid');
                todo_item_id = todo_item_id.split("_");
                var lastChar = todo_item_id[todo_item_id.length -1];
                var parent = $('.new-todo-text-box').parent();

                $.post("/new-sub-item",data).done(function( result ) {
                console.log("ok");
                $('.new-todo-text-box').remove();
                parent.append(result);
                append_new_subitem_textbox(lastChar)
                onclick_bind()

                })
            }
        }
    });


// Tried to use plain js instead of jquery

// Shortcut Functions
document.onkeyup = function(e) {
    // 78 = n (popup modal) and no text box active
    if(e.which == 78 && !$(e.target).closest("input, textarea").length){
        if(!document.getElementById('new_todo_modal').classList.contains("is-active")) {
            document.getElementById('new_todo_modal').classList.add("is-active");
            document.getElementById('id_todo_item').value = "";
            document.getElementById('id_todo_item').focus();
        }
    }
    else if(e.which == 27){
    // 23 = escape (exit modal)
        if(document.getElementById('new_todo_modal').classList.contains("is-active")) {
            document.getElementById('new_todo_modal').classList.remove("is-active");
        }
        // remove textbox to add subitem
        else if($(e.target).closest("input, textarea").length){
                $('.new-todo-text-box').remove();
        }
    }
}

// new sub todo item functions
var aclick = document.getElementsByClassName('new-sub-item');

Array.from(aclick).forEach(function(element) {
    element.addEventListener("click", handleClick,false);
  });


function handleClick(){
    // Create new span and text
    var new_list_item = document.createElement("span");
    var textbox = document.createElement("input");
    textbox.setAttribute("type", "text");
    textbox.setAttribute("name","subitem");
    textbox.setAttribute("data-todoid",this.id);
    textbox.setAttribute("class",'new-todo-text-box')
    // select the required elements
    var parent_id = this.getAttribute('data-todoid');
    var parent_element = document.getElementById(parent_id);
    var child_list = parent_element.querySelector('.sub-item');
    // append textbox to list
    new_list_item.appendChild(textbox);
    child_list.appendChild(new_list_item);
    child_list.querySelector('.new-todo-text-box').focus()
  }

function append_new_subitem_textbox(id){
    // Create new span and text
    var new_list_item = document.createElement("span");
    var textbox = document.createElement("input");
    textbox.setAttribute("type", "text");
    textbox.setAttribute("name","subitem");
    textbox.setAttribute("data-todoid",id);
    textbox.setAttribute("class",'new-todo-text-box')
    // select the required elements
    var parent_id = id;
    var parent_element = document.getElementById(parent_id);
    var child_list = parent_element.querySelector('.sub-item');
    // append textbox to list
    new_list_item.appendChild(textbox);
    child_list.appendChild(new_list_item);
    child_list.querySelector('.new-todo-text-box').focus()
}




});