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

$Addr = addslashes($_GET["Picture_Addr"]);
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

</head>
<body>
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<h1><a href="clothes_list.php"><- BACK </a></h1>
						<nav>
							<ul>
								<li><a href="Insert_DB.php?Picture_Addr=<? echo"$Addr"; ?>"><button>WEAR</button></a></p></li>
								
							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
					<?php
					echo "<img src='images/fulls/".$Addr.".jpg' class='image' width='device-width' height='device-height' />";
       					   ?>
					</div>
			</div>
</body>
<html>