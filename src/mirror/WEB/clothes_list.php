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

?>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     <!DOCTYPE HTML>
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
					$query = 'SELECT count(No) FROM Clothes_info';
					  $res = mysqli_query($conn,$query);
	        			  $row1 = $res -> fetch_array();
	      				$total_num = $row1[0];
						?>
						<h1>TOTAL <?php echo"$total_num"; ?> </h1>
						<nav>
							<ul>
								<li>TOP </li>
								<li>BOTTOM </li>
							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">
						<article class="thumb">
							<a href="images/fulls/1.jpg" class="image"><img src="images/thumbs/1.png" alt="" id="top" /></a>
							<h2>Top 1</h2>
							<p>Color : Orange Type : Top Texture: -.	<a href="select_clothe.html"><button>CHOOSE</button></a></p>
						</article>
						<article class="thumb">
							<a href="images/fulls/3.jpg" class="image"><img src="images/thumbs/3.png" alt="" /></a>
							<h2>Outer</h2>
							<p>Color : Black Type : Outer Texture: -.	<a href="select_clothe.html"><button>CHOOSE</button></p>
						</article>
						<article class="thumb">
							<a href="images/fulls/4.jpg" class="image"><img src="images/thumbs/4.png" alt="" /></a>
							<h2>Top 3</h2>
							<p>None</p>
						</article>
						<article class="thumb">
							<a href="images/fulls/6.jpg" class="image"><img src="images/thumbs/6.png" alt="" /></a>
							<h2>Top 5</h2>
							<p>None</p>
						</article>
						<article class="thumb">
							<a href="images/fulls/7.jpg" class="image"><img src="images/thumbs/7.png" alt="" /></a>
							<h2>Top 6</h2>
							<p>None</p>
						</article>
						<article class="thumb">
							<a href="images/fulls/8.jpg" class="image"><img src="images/thumbs/2.png" alt="" /></a>
							<h2>Top 7</h2>
							<p>None</p>
						</article>
						<article class="thumb">
							<a href="images/fulls/9.jpg" class="image"><img src="images/thumbs/8.png" alt="" /></a>
							<h2>Top8</h2>
							<p>None</p>
						</article>
						<article class="thumb">
							<a href="images/fulls/11.jpg" class="image"><img src="images/thumbs/11.png" alt="" /></a>
							<h2>Skirt</h2>
							<p>None</p>
						</article>
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