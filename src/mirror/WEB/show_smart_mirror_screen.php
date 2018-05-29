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

$query = "SELECT x,y,height,width,show_addr FROM Coordinate where position='lower'";
$res =  mysqli_query($conn,$query);
$row = mysqli_fetch_array($res);

$addr1 = $row2['show_addr'];
$addr2 = $row['show_addr'];

?>


<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="assets/css/show_clothe_css.css" />
<script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
<meta http-equiv="refresh" content="0.5">
<style>
 #lower{
  padding-left : <? echo $row['y']-100 ?>px;
  padding-top: <? echo $row['x']+350 ?>px;
  z-index : 1; }
 #upper{
    padding-left : <? echo $row2['y']+120 ?>px;
    padding-top: <? echo $row2['x']+500 ?> px;
    z-index : 4;}
</style>
</head>
<body>
  <p style="color:red" id ="table">
</p>
  <?
  $Y =date(" Y");
  $m_d =date("m.d");
  $h_i =date("h:i");
  echo "<p style='font-size:500%; font-family: Sans-Serif'><b> $Y <br> $m_d <br> $h_i</b></p>";
  ?>
<div id="upper" style="position:fixed"><img src="images/thumbs/<? echo $addr1; ?>.png" height"<? echo $row2['height']+100?>" width="<? echo  $row2['width']+400?>" alt=""/></div>
<div id="lower" style="position:fixed"><img src="images/thumbs/<? echo $addr2; ?>.png" height"<? echo $row['height']?>" width="<? echo  $row['width']+500?>" alt=""/></div>
</body>
</html>
