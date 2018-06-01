$('#cancle1').hover(function(){
  $('#call').text('버튼을 누르면 선택한 상의가 취소됩니다.');},
  function(){  $('#call').text('현재 선택한 옷입니다. 다른 옷을 입으시려면 Clothes List를 눌러주세요.');
});

$('#cancle2').hover(function(){
  $('#call').text('버튼을 누르면 선택한 하의가 취소됩니다.');},
  function(){  $('#call').text('현재 선택한 옷입니다. 다른 옷을 입으시려면 Clothes List를 눌러주세요.');
});

$('#recomment').hover(function(){
  $('#call').text('선택한 옷과 어울리는 코디를 추천해줍니다. 그림을 누르시면 입을 수 있습니다.');},
  function(){  $('#call').text('현재 선택한 옷입니다. 다른 옷을 입으시려면 Clothes List를 눌러주세요.');
});


$('#cancle1').click(function(){
  $('#up').remove();
});

$('#cancle2').click(function(){
  $('#down').remove();
});
