<?php
$status = array ( 0 );
//set pins mode to output
for ($i = 0; $i <= 7; $i++ ) 
{
     system ( "gpio mode ".$i." out" );
}
for ($i = 0; $i <= 7; $i++ )
{
    if ($i = 0) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 1)
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 2) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 3) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 4) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 5) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 6) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
    elseif ($i = 7) 
    {
        system ( "gpio write ".$i." 1" );
        sleep ( 8 );
        system ( "gpio write ".$i." 0" );
    }
}
//reads and prints the LEDs status
for ($i = 0; $i <= 7; $i++ ) 
{
     exec ( "gpio read ".$i, $status );
     echo ( $status[0] );
}
?>