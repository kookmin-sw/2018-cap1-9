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


?>
<!DOCTYPE HTML>
<html>
<head>
 <title>Select Clothe</title>
     		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
    <script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
</head>
<body>
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<h1><a href="clothes_list.php"><- BACK </a></h1>
						<nav>
							<ul>
								<li><a href="Insert_DB.php?No=<? echo"$No"; ?>"><button>WEAR</button></a></p></li>

							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
            <?php
					echo "<img src='images/fulls/".$Addr.".jpg' class='image' width='device-width' height='device-height' style='padding-top:10%; padding-left:15%'/>";
          ?>
					</div>
			</div>
      <script src="getParameter.js"></script>
</body>
<html>
