/*------------------------------------*\
    JURY VOTING
\*------------------------------------*/

// Checkbox selects
$('.btn-group-toggle>label').click(function() {
  $(this).toggleClass('active');
  $(this).find('input').toggleAttr("checked");
});

// hide extra toxicity action questions
$('#panelAction').hide();

// hide Jury results until ready
// $('#juryDecision').hide();

// Individual Slider
var sliderIndiv = $('#sliderIndiv').slider({
  rangeHighlights: [
    {'start':0, 'end': 4, 'class': 'slider-low'},{'start':4, 'end': 8, 'class': 'slider-med'}, {'start':8, 'end': 10, 'class': 'slider-high'}
  ],
  min: 0,
  max: 10,
  step: 0.5,
  value: 0
});

// Jury Slider
var sliderJury = $("#sliderJury").slider({
  rangeHighlights: [
    {'start':0, 'end': 4, 'class': 'slider-low'},{'start':4, 'end': 8, 'class': 'slider-med'}, {'start':8, 'end': 10, 'class': 'slider-high'}
  ],
  min: 0,
  max: 10,
  step: 0.5,
  value: 0,
  precision: 2
});


// Get individual score
sliderIndiv.on("change", function(slideEvt) {
  scoreIndiv = slideEvt.value.newValue;
  scoreJury = scoreIndiv / 6;

  // update score text
  $("#indivScore").text(scoreIndiv);
  // $("#juryScore").text(scoreJury.toFixed(2));

  // // update jury DECISION
  // sliderJury.slider('setValue', scoreJury);
  // $('#juryDecision').show();

  // activate submit button
  $("#submit").removeClass("btn-secondary");
  $("#submit").removeAttr("disabled");
  $("#submit").addClass("btn-primary");

  if (scoreIndiv >= 8) {
    // TOXIC
    $("#panelAction").show(200);
    $("#indivScoreLabel").removeClass("badge-warning badge-primary");
    $("#indivScoreLabel").html("Toxic").addClass("badge-danger");
  } else if (scoreIndiv >= 4 && scoreIndiv < 8) {
    // BORDERLINE
    $("#panelAction").show(200);
    $("#indivScoreLabel").removeClass("badge-danger badge-primary");
    $("#indivScoreLabel").html("Borderline").addClass("badge-warning");

  } else {
    // OK
    $("#panelAction").hide();
    $("#indivScoreLabel").removeClass("badge-warning badge-danger");
    $("#indivScoreLabel").html("OK").addClass("badge-primary");
  }
});
