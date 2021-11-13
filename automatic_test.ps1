[int]$times=Read-Host "Each test number of execution"
[int]$each_time=Read-Host "Minutes to next execution"

while($True){
    Write-Host "`nStarting execution" -ForegroundColor Green
    python ex.py $times
    $date=Get-Date
    Write-Host "Next test on " $date.AddMinutes($each_time) -ForegroundColor Green
    Start-Sleep -Seconds ([int]$each_time*60)
    Clear-Host
}