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

$query2 = 'SELECT Picture_Addr FROM Clothes_Info';
$res2 =  mysqli_query($conn,$query2);

$que = 'SELECT upper,lower FROM Clothes_Log order by No desc';
$res =  mysqli_query($conn,$que);

$sql = "UPDATE Coordinate SET show_addr = 'black' WHERE position = 'upper'";
if (mysqli_query($conn,$sql)){
  }
  else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
  }
$sql2 = "UPDATE Coordinate SET show_addr = 'black' WHERE position = 'lower'";
  if (mysqli_query($conn,$sql2)){
    }
    else{ echo "Error: " .$sql2 . "<br>" . mysqli_error($conn);
    }


?>
<!DOCTYPE HTML>
<html>
	<head>
		<title>MAIN VT</title>
		<meta charset="utf-8" />

		<!--[if lte IE 8]><script src="Oassets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="Oassets/css/main.css" />
      <script type="text/javascript" src="http://code.jquery.com/jquery-2.2.3.min.js"></script>
		<noscript><link rel="stylesheet" href="Oassets/css/noscript.css" /></noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="Oassets/css/ie8.css" /><![endif]-->
	</head>
	<body>
		<!-- Wrapper-->
    <div id="wrapper">

      <!-- Nav -->
        <nav id="nav">
          <a href="#me" class="icon fa-home active"><span>Home</span></a>
          <a href="#log" class="icon fa-folder"><span>Log</span></a>
          <a href="#manual" class="icon fa-envelope"><span>Manual</span></a>
        </nav>

      <!-- Main -->
        <div id="main">

          <!-- Me -->
            <article id="me" class="panel">
              <header style="margin-top:-6%">
                <h1>VT PROJECT</h1>
                <p style="font-size:90%"><br>VT 프로젝트는 사용자가 가진 옷의 리스트들을 보여줍니다.<br>
	   사용자가 원하는 옷을 선택하면 거울 위로 해당 옷이 나타납니다.<br><b><i>VT PROJECT</i></b>를 시작하려면 화살표를 눌러주세요.
                  </p>
              </header>
              <a href="VT_list.php" class="jumplink pic">
                <span class="arrow icon fa-chevron-right"><span>See my log</span></span>
              </a>
            </article>

          <!-- Work -->
            <article id="log" class="panel">
              <header>
                <h2>Log</h2>
              </header>
              <p>
                최근 선택한 옷의 기록을 확인할 수 있습니다.<br>
                단, 기록은 최근 순으로 12개까지만 보여집니다.
              </p>
              <section>
                <div class="row">
                  <?php
                  while ($row10 = $res->fetch_assoc())

                  {
                   echo"<div class='4u 12u$(mobile)'>
                      <a href='#' class='image fit'><img src='images/thumbs/".$row10['upper'].".png' alt=''></a>
                        <a href='#' class='image fit'><img src='images/thumbs/".$row10['lower'].".png' alt=''></a>
                    </div>";
                  }
                    ?>
                </div>
              </section>
            </article>

          <!-- Contact -->
            <article id="manual" class="panel">
              <header>
                <h2>VT Manual</h2>
              </header>
              <div >
              <img src='images/p1.png' width='100%' alt=''>
              <img src='images/p2.png' width='100%' alt=''>
              <img src='images/p3.png' width='100%' alt=''>
              <img src='images/p4.png' width='100%' alt=''>
              <img src='images/p5.png' width='100%' alt=''>
              <img src='images/p6.png' width='100%' alt=''>
              <img src='images/p7.png' width='100%' alt=''>
              <img src='images/p8.png' width='100%' alt=''>
            </div>
             </article>

        </div>




		<!-- Scripts -->
			<script src="Oassets/js/jquery.min.js"></script>
<script src="Oassets/js/skel.min.js"></script>
			<script src="Oassets/js/skel-viewport.min.js"></script>
			<script src="Oassets/js/util.js"></script>
			<!--[if lte IE 8]><script src="Oassets/js/ie/respond.min.js"></script><![endif]-->
			<script src="Oassets/js/main.js"></script>

	</body>
</html>
