$each_time=30
$test_per_time=5

while ($true) {
    python executor.py $test_per_time
    $time=Get-Date
    write-Host "Next operation on" $time.AddMinutes($each_time)
    Start-Sleep -s ($each_time*60)
    clear
}