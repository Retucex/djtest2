$(document).ready(function(){
    var choice_count = 1;
    $('#button_add_choice').click(function(){
        var choice = "<li><input type='text' name='choice" + choice_count + "' id='choice" + choice_count + "' /></li>";
        choice_count += 1

        $('#list_choices').after(choice);
    });
});