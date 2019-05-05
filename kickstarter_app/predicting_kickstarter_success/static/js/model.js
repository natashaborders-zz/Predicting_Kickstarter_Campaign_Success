/* This function is called when the submit button is pressed/
 *
 * See the "on" attribute of the submit button */
function process(){
  console.log('hi');

  // we have really long feature names =(
  feature = {
    'Goal (USD)': $('#goal').val(),
    'Is this campaign a staff pick? (1 for yes, 0 for no)':  $('#staff_pick_True').val(),
    'Campaign Length (in days)': $('#cam_length').val(),
    'Campaign Blurb Length (in number of words)':  $('#blurb_length').val()
    'Is this campaign based in the US? (1 for yes, 0 for no)':  $('#country_US').val()
  }

  // Call our API route /predict_api via the post method
  // Our method returns a dictionary.
  // If successful, pass the dictionary to the function "metis_success"
  // If there is an error, pass the dictionary to the functoin "metis_error"
  // Note: functions can have any name you want; to demonstrate this we put
  //       metis_ at the beginning of each function.
  $.post({
    url: '/predict_api',
    contentType: 'application/json',
    data: JSON.stringify(feature),
    success: result => metis_success(result),
    error: result => metis_error(result)
  })
}

function ourRound(val, decimalPlaces=1){
  // Javascript rounds to integers by default, so this is a hack
  // to round to a certain number of decimalPlaces
  const factor = Math.pow(10, decimalPlaces)
  return Math.round(factor*val)/factor
}

/* Here "result" is the "dictionary" (javascript object)
 * that our get_api_response function returned when we called
 * the /predict_api function
 *
 * Here we select the "results" div and overwrite it
 */
function metis_success(result){
  $('#results').html(`The most likely class is ${result.most_likely_class_name}
                      with probability ${ourRound(100*result.most_likely_class_prob)}%`);

  const all_results = result.all_probs.map( (data) => `${data.name}: ${ourRound(100*data.prob)}`)
  $('#list_results').html(all_results.join('%<br>') + '%');

  // only included in predictor_javascript_slider_graph.html
  // otherwise does nothing.
  modifyDivs(result.all_probs);
}

function metis_error(result){
  console.log(result);
  alert("I don't know what you did");
}
