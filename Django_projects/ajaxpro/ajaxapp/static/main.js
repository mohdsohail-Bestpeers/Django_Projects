$(document).ready(function(){
    $(".btn").click(function(){
      $.ajax({
          url: '',
          type: 'get',
          data:{
                button_text: $(this).text()
          },
          success: function(response){
              $(".btn").text(rsponse.seconds)
          }
      });
    });
  });
  