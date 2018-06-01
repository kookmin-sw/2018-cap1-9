
<?
$db_host ="localhost";
$db_user = "root";
$db_password ="1234";
$db_name = "VT";
$conn = mysqli_connect($db_host,$db_user,$db_password,$db_name);

if(!$conn){
  die("connetction failed:" . mysqli_connect_error());
  }

  $position = addslashes($_GET["position"]);

  $query = "SELECT show_addr FROM Coordinate where position = '$position '" ;
  $res =  mysqli_query($conn,$query);
  $row = $res -> fetch_array();
  $show_addr = $row[0];

  $query1 = "SELECT No FROM Clothes_Info where Picture_Addr = $show_addr " ;
  $res1 =  mysqli_query($conn,$query1);
  $row1 = $res1 -> fetch_array();
  $show_no = $row1[0];


$sql = "UPDATE Coordinate SET show_addr ='black' WHERE position = '$position'";
if (mysqli_query($conn,$sql)){
  }
    else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
    }

  mysqli_close($conn);

  ?>
  <html>
   <head>
      <script type="text/javascript">
        location.href='select_clothe.php?No=<? echo $show_no ;?>&Picture_Addr=black';
      </script>
   </head>

  </html>
