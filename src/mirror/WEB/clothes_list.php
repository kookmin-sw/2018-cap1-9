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


?>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      <!DOCTYPE HTML>
<html>
	<head>
		<title>Clothes List</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<script src="assets/js/ie/html5shiv.js"></script>
		<link rel="stylesheet" href="assets/css/main.css" />
		<link rel="stylesheet" href="assets/css/ie9.css" />
		<link rel="stylesheet" href="assets/css/ie8.css" />
	</head>
	<body>

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
					<?php
					$query = 'SELECT count(No) FROM Clothes_Info';
					  $res = mysqli_query($conn,$query);
	        			  $row1 = $res -> fetch_array();
	      				$total_num = $row1[0];
                						?>
						<h1>TOTAL <?php echo"$total_num"; ?> </h1>
            <nav>
							<ul>
								<li><a href="#top">TOP</a> <a href="#bottom">BOTTOM</a> </li>
							</ul>
            </nav>
					</header>
          <?php
          $query2 = 'SELECT No,Color,Kind,Picture_Addr FROM Clothes_Info';
          $res2 =  mysqli_query($conn,$query2);
            ?>
				<!-- Main -->
					<div id="main">
            <?php
            while ($row2 = $res2->fetch_assoc())

						{
					 echo "<article class='thumb'>
                 <a href='images/fulls/".$row2['Picture_Addr'].".jpg' class='image'";
                 if ($row2['No'] == 1){
                   echo"id='#top'";
                 }
                 elseif($row2['No'] == $total_num) {
                   echo"id='#bottom'";
                 }
                   echo"><img src='images/thumbs/".$row2['Picture_Addr'].".png' alt='' /></a>
                 <h2>" .$row2['Kind']."</h2>";
                 echo"<p> Color :".$row2['Color']."  Type :".$row2['Kind']."<a href='select_clothe.php?No=".$row2['No']."&Picture_Addr=".$row2['Picture_Addr']."' style='padding-left:30%'><button >CHOOSE</button></a></p></article> ";

						}
            ?>
					</div>

			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.poptrox.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/ie/respond.min.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>
