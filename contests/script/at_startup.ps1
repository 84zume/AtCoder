$contest_name = $Args[0]
$src_dir = "contests/src/$contest_name"
mkdir $src_dir
Set-Location $src_dir
oj-prepare https://atcoder.jp/contests/${contest_name}