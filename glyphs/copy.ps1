param(
    $from,
    $to
)

if($from -eq $NULL -or $to -eq $NULL){
    exit
}

$n = [Convert]::ToInt64($from, 16)
$end = [Convert]::ToInt64($to, 16)

if ($n -gt $end) {
    exit
}

while($n -le $end) {
    cp 'u.svg' ('u'+[Convert]::ToString($n,16)+'.svg')
    $n++
}
