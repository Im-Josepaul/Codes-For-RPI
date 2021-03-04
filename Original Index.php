<?php
$status = array ( 0 );
//set pins mode to output
for ($i = 0; $i <= 7; $i++ ) {
     system ( "gpio mode ".$i." out" );
}
//turns on the LEDs
for ($i = 0; $i <= 7; $i++ ) {
     system ( "gpio write ".$i." 1" );
}
//reads and prints the LEDs status
for ($i = 0; $i <= 7; $i++ ) {
     exec ( "gpio read ".$i, $status );
     echo ( $status[0] );
}
//waits 2 seconds
sleep ( 2 );
//turns off the LEDs
for ($i = 0; $i <= 7; $i++ ) {
     system ( "gpio write ".$i." 0" );
}
?>
