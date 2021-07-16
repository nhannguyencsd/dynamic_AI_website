var inner_skills = $('.nn-inner-skill');
for(i=0; i < inner_skills.length; i++) {
    $(inner_skills[i]).css({"width": $(inner_skills[i]).val() + "%", "background-color": "#4caf50"});
}

if ($("#category").val() === "AI") {
        $(".nn-ai-label").show();
        $(".nn-ai").show();
} else {
    $(".nn-ai-label").hide();
    $(".nn-ai").hide();
};
$("#category").on('change', function() {
    if ($(this).val() === "AI") {
        $(".nn-ai-label").show();
        $(".nn-ai").show();
    } else {
        $(".nn-ai-label").hide();
        $(".nn-ai").hide();
        $("#model_name").val("");
        $("#nn-input").val("");
        $("#weight").val("");
        $("#aidotpy").val("");
    }
});

if ($("#ask_update").val() == "Yes") {
    $(".nn-ai-label").show();
    $(".nn-ai").show();
} else {
    $(".nn-ai-label").hide();
    $(".nn-ai").hide();
};
$("#ask_update").on('change', function() {
    if ($(this).val() === "Yes") {
        $(".nn-ai-label").show();
        $(".nn-ai").show();
    } else {
        $(".nn-ai-label").hide();
        $(".nn-ai").hide();
    }
});

if ($(this).width() !== width) {
    var image_width = $('.nn-thumbnail').width();
    $('.nn-thumbnail').css({'height': image_width*0.65 + 'px'});
}
var width = $(window).width();
$(window).on('resize', function() {
    if ($(this).width() !== width) {
        var image_width = $('.nn-thumbnail').width();
        $('.nn-thumbnail').css({'height': image_width*0.65 + 'px'});
    }
});

$(".nn-file-select").click(function(){
    $(".nn-one-click").css({
        "pointer-events": "initial",
        "display": "block",
    });
});

$(".nn-one-click").click(function() {
    $(this).css({
        "pointer-events": "none",
        "display": "none"
    });
});

$('.nn-no-input').remove();

$(".nn-solution-button").click(function() { 
    if ($(this).text() == "Solution") { 
        $(this).text("Hide answer"); 
        $(".nn-solution-text").show()
    } else { 
        $(this).text("Solution");
        $(".nn-solution-text").hide()
    }; 
});
