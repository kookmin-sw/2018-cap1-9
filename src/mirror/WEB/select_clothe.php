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

$No = addslashes($_GET["No"]);
$Addr = addslashes($_GET["Picture_Addr"]);

$query = "SELECT position FROM Clothes_Info where No = $No " ;
$res =  mysqli_query($conn,$query);
$row = $res -> fetch_array();
$position = $row[0];

if($position == 'upper'){
 $sql = "UPDATE Coordinate SET show_addr = $Addr WHERE position = 'upper'";
if (mysqli_query($conn,$sql)){
  }
  else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
  }
}
if($position == 'lower'){
  $sql = "UPDATE Coordinate SET show_addr = $Addr WHERE position = 'lower'";
  if (mysqli_query($conn,$sql)){
    }
    else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
    }
}

exec("python matrix_algorithm.py");

$que = "SELECT show_addr FROM Coordinate where position='upper'" ;
$res3 =  mysqli_query($conn,$que);
$row3 =  mysqli_fetch_array($res3);
$upper_addr = $row3[0];

$que2 = "SELECT show_addr FROM Coordinate where position='lower'" ;
$res4 =  mysqli_query($conn,$que2);
$row4 =  mysqli_fetch_array($res4);
$lower_addr = $row4[0];

?>
<!DOCTYPE HTML>
<html>
<head>
 <title>Select Clothe</title>
     		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->

		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
    <script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
    <link rel="stylesheet" href="assets/css/main.css" />
    <style>
    .button_css{
     font-family: Arial, Helvetica, sans-serif;
     font-size: 17px;
     color: #ffffff;
     padding: 2px 20px;
     background: -moz-linear-gradient(
       top,
       #6b6b6b 0%,
       #000000);
     background: -webkit-gradient(linear, left top, left bottom,from(#6b6b6b),to(#000000));
     -moz-border-radius: 30px;
     -webkit-border-radius: 30px;
     border-radius: 30px;
     border: 1px solid #000000;
     -moz-box-shadow:
       0px 1px 3px rgba(000,000,000,0.5),
       inset 0px 0px 1px rgba(255,255,255,0.7);
     -webkit-box-shadow:
       0px 1px 3px rgba(000,000,000,0.5),
       inset 0px 0px 1px rgba(255,255,255,0.7);
     box-shadow:
       0px 1px 3px rgba(000,000,000,0.5),
       inset 0px 0px 1px rgba(255,255,255,0.7);
     text-shadow:
       0px -1px 0px rgba(000,000,000,0.4),
       0px 1px 0px rgba(255,255,255,0.3);
    margin-left: 45%;
    margin-top : 10%;
    width: 15%;
    position:fixed;
    }
    #cancle{

    }
    </style>
</head>
<body style="background-color: white">
			<div id="wrapper">

				<!-- Header -->
					<header id="header" style="background-image:url(images/배경.png)" >
						<h1><a href="clothes_list.php" style='color:black'><- clothes list </a></h1>
            <span style='color:white; font-size:130%; margin-left:25%'> 현재 선택한 옷입니다. 선택을 취소하려면 취소버튼을 눌러주세요.</span>
						<nav>
							<ul>
								<li><a href="Insert_DB.php?No=<? echo"$No";?>"><button>WEAR</button></a></p></li>

							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
            <?php
					echo "<div style='position:fixed; margin-left :8%;z-index : 4;'><img src='images/thumbs/".$upper_addr.".png' class='image' width='70%' style=' z-index:-1000; padding-left:3%'/></div>";
          echo "<div style='position:fixed; margin-top:14%; margin-left :8%; z-index:1'><img src='images/thumbs/".$lower_addr.".png' class='image' width='65%'/></div>";
          ?>

					</div>
          <button class='button_css' id="cancle"  onclick="choose()">상의 취소</button>
          <button class='button_css' id="cancle"  onclick="choose()" style='margin-top:30%;'>하의 취소</button>

          <div style='position:fixed;margin-left:80%; background-color:black; width:35%; height:95%;'>
            <?php $fopen = fopen("list.txt", "r"); $list_1 = fgets($fopen); $list_2 = fgets($fopen); $list_3 = fgets($fopen); fclose($fopen);  ?>
            <div style="color:white; font-size:150%;margin-left:2%;">코디 추천</div>
            <div style="color:white; font-size:120%;margin-left:2%;">1순위<img src='images/thumbs/<? echo $list_1; ?>.png' width='35%' height:'25%' ></div>
            <div style="color:white; font-size:120%;margin-left:2%;">2순위<img src='images/thumbs/<? echo $list_2; ?>.png' width='35%' height:'25%'></div>
            <div style="color:white; font-size:120%;margin-left:2%;">3순위<img src='images/thumbs/<? echo $list_3; ?>.png' width='35%' height:'25%'></div>
          </div>
<script>
function choose() {
    document.getElementById("choose").style.color = "red";
}
</script>
			</div>
</body>
<html>
