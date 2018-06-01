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

?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>Clothes List</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="Massets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="Massets/css/main.css" />
		<!--[if lte IE 9]><link rel="stylesheet" href="Massets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="Massets/css/ie8.css" /><![endif]-->
	</head>
	<body>
		<?php
		$query = 'SELECT count(No) FROM Clothes_Info';
			$res = mysqli_query($conn,$query);
						$row1 = $res -> fetch_array();
					$total_num = $row1[0];
											?>
      <div style='opacity: 0.8;position:fixed;background-image:url(images/배경.png);text-align:center;color:white;font-size: 200%;vertical-align: baseline;width:100%;height:10%;z-index:10000;display: block '>
        <span style="margin-right:20%"><a href="main.php" style='text-decoration:none'><- BACK</a></span>
        입어보고싶은 옷을 선택해주세요. <span style='margin-left:14%'><b>TOTAL<?php echo " $total_num"; ?></b></span></div>
		<!-- Wrapper -->
			<div id="wrapper">
                         <h1 style='opacity:0'>'</h1>
				<!-- Main -->
				<?php
				$query2 = 'SELECT No,Color,Kind,Picture_Addr FROM Clothes_Info';
				$res2 =  mysqli_query($conn,$query2);
					?>
					
<div id="main">
						<div class="inner">
							<header>
	<h1>Clothes List </h1>
								<p></p>
							</header>
							<section class="tiles">

									<?php
			            while ($row2 = $res2->fetch_assoc())
                  {
                    echo "<article class='style1'><div><img src='images/thumbs/".$row2['Picture_Addr'].".png' alt='' width='90%'/></div>";
                    echo "<a href='select_clothe.php?No=".$row2['No']."&Picture_Addr=".$row2['Picture_Addr']."'><h2 style='color:black;margin-top:42%;padding-top:60%'>".$row2['Kind']."</h2><div style='color:black;'> Color :".$row2['Color']."  Type :".$row2['Kind']."</div><div class='content'>";
                    echo "</div></a></article>";
									}
			            ?>
							</section>
						</div>
					</div>

			</div>

		<!-- Scripts -->
			<script src="Massets/js/jquery.min.js"></script>
			<script src="Massets/js/skel.min.js"></script>
			<script src="Massets/js/util.js"></script>
			<!--[if lte IE 8]><script src="Massets/js/ie/respond.min.js"></script><![endif]-->
			<script src="Massets/js/main.js"></script>

	</body>
</html>
