<html>
<head>
	<meta charset = "UTF-8">
	<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.1/dist/leaflet.css" integrity="sha256-sA+zWATbFveLLNqWO2gtiw3HL/lh1giY/Inf1BJ0z14=" crossorigin="" />
	<title>Teltonika Map</title>
</head>
<body>
	<style>
		#map {
			width: 100%;
			height: 97vh;
		}
	</style>
	<div id="map"></div>
	<script src="https://unpkg.com/leaflet@1.9.1/dist/leaflet.js" integrity="sha256-NDI0K41gVbWqfkkaHj15IzU7PtMoelkzyKp8TOaFQ3s=" crossorigin=""></script>
	<script>
		let mapOptions = {
			center:[41.0931499, 29.087595],
			zoom:10
		}

		let map = new L.map('map' , mapOptions);

		let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
		map.addLayer(layer);
	</script>
	
	<?php 
		include 'server.php';
		date_default_timezone_set("Etc/GMT-3");
		$conn = OpenCon();
		$i = 1;
		
		$sql = "SELECT Data_Packet_ID, Timestamp, Longitude, Latitude FROM data_packet";
		$result = mysqli_query($conn, $sql);
		echo '<script>var locs = [];</script>';
		while($row = mysqli_fetch_assoc($result))
		{
			$timestamp = hexdec($row["Timestamp"]);
			$timestamp = substr($timestamp, 0, 10);
			$timestamp = date("H:i:s d/m/Y", $timestamp,);
			$longitude = hexdec($row["Longitude"]);
			$latitude = hexdec($row["Latitude"]);
			$data_id = $row["Data_Packet_ID"];
			$new_latitude = substr_replace($latitude, ".", -7 , 0);
			$new_longitude = substr_replace($longitude, ".", -7 , 0);
			$io_sql = "SELECT Data_ID, IO_ID, Value FROM io WHERE Data_ID = '" . $data_id . "'";
			$io_result = mysqli_query($conn, $io_sql);
			$io_list = array();
			while($io_row = mysqli_fetch_assoc($io_result))
			{
				$IO_ID = $io_row["IO_ID"];
				$Value = $io_row["Value"];
				$io_desc_sql = "SELECT IO_ID, Property_Name, Description FROM io_desc WHERE IO_ID = '" . $IO_ID . "'";
				$io_desc_result = mysqli_query($conn, $io_desc_sql);
				while($io_desc_row = mysqli_fetch_assoc($io_desc_result))
				{
					$io_name = $io_desc_row["Property_Name"];
					$io_desc = $io_desc_row["Description"];
				}
				$temp = ["IO_ID"=>$IO_ID, "IO_Name"=>$io_name, "Value"=>$Value . "<br>"];
				array_push($io_list, $temp);
			}
			
			$json = json_encode($io_list);
			$json = str_replace('"','', (string) $json);
			$json = str_replace(',',' ', (string) $json);
			$json = str_replace('}','', (string) $json);
			$json = str_replace('{','', (string) $json);
			$json = str_replace('[','', (string) $json);
			$json = str_replace(']','', (string) $json);
			
			echo "<script>
				locs.push([" . $new_latitude . ", " . $new_longitude . "]);
				L.marker([" . $new_latitude . ", " . $new_longitude . "]).bindPopup('Time: " . $timestamp . "<br>Location: [" . $new_latitude . ", " . $new_longitude . "]<br>" . $json . "',{minWidth : 350}).addTo(map);
			</script>";
			$i = $i + 1;
		}
		echo "<script>
		var polyline = L.polyline(locs, {color: 'red'}).addTo(map);
		</script>";
		CloseCon($conn);
	?>
</body>
</html>