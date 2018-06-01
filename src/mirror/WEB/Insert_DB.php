
<?
$db_host ="localhost";
$db_user = "root";
$db_password ="1234";
$db_name = "VT";
$conn = mysqli_connect($db_host,$db_user,$db_password,$db_name);

if(!$conn){
  die("connetction failed:" . mysqli_connect_error());
  }

$upper = addslashes($_GET["upper"]);
$lower = addslashes($_GET["lower"]);

$query = 'SELECT count(No) FROM Clothes_Log';
  $res = mysqli_query($conn,$query);
        $row1 = $res -> fetch_array();
      $total_num = $row1[0]+1;
$date =date("Y-m-d/H:i");

$sql = "INSERT INTO Clothes_Log (No,upper,lower,date) VALUES ('$total_num+1','$upper','$lower','$date')";
if (mysqli_query($conn,$sql)){
  }
  else{ echo "Error: " .$sql . "<br>" . mysqli_error($conn);
  }

mysqli_close($conn);

?>
<html>
 <head>
    <script type="text/javascript">
       location.href='main.php';
    </script>
 </head>

</html>
