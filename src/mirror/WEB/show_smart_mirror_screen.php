<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="assets/css/show_clothe_css.css" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
<meta http-equiv="refresh" content="1">
<script>
$(document).ready(function(){
        $.ajax({
            url : "",
            dataType : "json",
            type : "get",
            success : function(data){
                $("table").html("<tr><th>x</th><th>y</th><th>width</th><th>height</th></tr>");
                var show = "";
                $.each(data,function(index, item){
                    show += "<tr><td>"+item.x+"</td>";
                    show += "<td>"+item.y+"</td>";
                    show += "<td>"+item.width+"</td>";
                    show += "<td>"+item.height+"</td></tr>";
                });
                $("table").append(show);
            }
        });
    });
});
</script>
</head>
<body>
  <table>

  </table>
  <?
  $time =date("Y-M-d h:m:s");
  echo "<p>$time</p>";
  ?>
<p><img src="images/thumbs/1.png" alt=""/></p>
<script type="text/javascript" src="getPrameter.js">
</body>
</html>
