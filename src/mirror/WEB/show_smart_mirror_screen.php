<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "VT";

// Create connection
 $conn = mysqli_connect($servername, $username, $password, $dbname);
 // Check connection
  if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$query2 = "SELECT x,y,height,width,show_addr FROM Coordinate where position='upper'";
$res2 =  mysqli_query($conn,$query2);
$row2 = mysqli_fetch_array($res2);

$addr =  $row2['show_addr'];

?>

<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="assets/css/show_clothe_css.css" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
<meta http-equiv="refresh" content="1">
<style>
 #img{
  padding-left : <? echo $row2['y']?>%;
  padding-top: <? echo $row2['x']?>%;
 }
</style>
</head>
<body>
  <p style="color:red" id ="table">
</p>
  <?
  $Y =date(" Y");
  $m_d =date("m.d");
  $h_i =date("h:i");
  echo "<p style='font-size:350%; font-family: Sans-Serif'><b> $Y <br> $m_d <br> $h_i</b></p>";
  ?>
<p id="img"><img src="images/thumbs/<? echo $addr; ?>.png" height"<? echo $row2['height']?>" width="<? echo  $row2['width']?>" alt=""/></p>
</body>
</html>
