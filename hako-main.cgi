#!/usr/bin/perl
# ↑はサーバーに合わせて変更して下さい。
# perl5用です。

#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# メインスクリプト
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# いのら諸島
#----------------------------------------------------------------------

require ('hako-ini.cgi');

#----------------------------------------------------------------------
# これ以降のスクリプトは、変更されることを想定していませんが、
# いじってもかまいません。
# コマンドの名前、値段などは解りやすいと思います。
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# 各種定数
#----------------------------------------------------------------------
# このファイル
$HthisFile = "$baseDir/hako-main.cgi";

# 地形番号
$HlandSea		= 0;  # 海
$HlandWaste		= 1;  # 荒地
$HlandPlains	= 2;  # 平地
$HlandTown		= 3;  # 町系
$HlandForest	= 4;  # 森
$HlandFarm		= 5;  # 農場
$HlandFactory	= 6;  # 工場
$HlandBase		= 7;  # ミサイル基地
$HlandDefence	= 8;  # 防衛施設
$HlandMountain	= 9;  # 山
$HlandMonster	= 10; # 怪獣
$HlandSbase		= 11; # 海底基地
$HlandOil		= 12; # 海底油田
$HlandMonument	= 13; # 記念碑
$HlandHaribote	= 14; # ハリボテ

# コマンド
$HcommandTotal = 36; # コマンドの種類

# コマンド分割
# このコマンド分割だけは、自動入力系のコマンドは設定しないで下さい。
@HcommandDivido = 
		(
		'開発,0,10',  # 計画番号00〜10
		'建設,11,24', # 計画番号11〜30
		'いのら,25,34',# 計画番号25〜34
		'攻撃,35,40', # 計画番号31〜40
		'運営,41,60'  # 計画番号41〜60
		);
# 注意：スペースは入れないように
# ○→		'開発,0,10',		# 計画番号00〜10
# ×→		'開発, 0  ,10  ',	# 計画番号00〜10

# 計画番号の設定
# 整地系
$HcomPrepare  = 01; # 整地
$HcomPrepare2 = 02; # 地ならし
$HcomReclaim  = 03; # 埋め立て
$HcomDestroy  = 04; # 掘削
$HcomSellTree = 05; # 伐採
$HcomFastRec  = 06; # 高速埋め立て
$HcomFastDes  = 07; # 高速掘削

# 作る系
$HcomPlant		= 11; # 植林
$HcomFarm		= 12; # 農場整備
$HcomFactory	= 13; # 工場建設
$HcomMountain	= 14; # 採掘場整備
$HcomBase		= 15; # ミサイル基地建設
$HcomDbase		= 16; # 防衛施設建設
$HcomSbase		= 17; # 海底基地建設
$HcomMonument	= 18; # 記念碑建造
$HcomHaribote	= 19; # ハリボテ設置
$HcomFastPlant	= 20; # 高速植林
$HcomFastFarm	= 21; # 高速農場整備
$HcomFastFact	= 22; # 高速工場建設
$HcomFastBase	= 23; # 高速ミサイル基地建設
$HcomFastDbase	= 24; # 高速防衛施設建設

# いのら系
$HcomSchool	  = 25; # いのら学校
$HcomEste	  = 26; # いのらエステ
$HcomTreaning = 27; # いのらジム
$HcomRest	  = 28; # いのら療養
$HcomPlay	  = 29; # いのら遊戯

# 発射系
$HcomMissileNM  = 35; # ミサイル発射
$HcomMissilePP  = 36; # PPミサイル発射

# 運営系
$HcomDoNothing	= 41; # 資金繰り
$HcomSell		= 42; # 食料輸出
$HcomMoney		= 43; # 資金援助
$HcomFood		= 44; # 食料援助
$HcomPropaganda	= 45; # 誘致活動
$HcomGiveup		= 46; # 島の放棄

# 自動入力系
$HcomAutoPrepare  = 61; # フル整地
$HcomAutoPrepare2 = 62; # フル地ならし
$HcomAutoDelete   = 63; # 全コマンド消去

# 順番
@HcomList =
	($HcomPrepare, $HcomSell, $HcomPrepare2, $HcomReclaim, $HcomDestroy,
	 $HcomSellTree, $HcomFastRec, $HcomFastDes, $HcomPlant, $HcomFarm, 
	 $HcomFactory, $HcomMountain, $HcomBase, $HcomDbase, $HcomFastPlant,
	 $HcomFastFarm, $HcomFastFact, $HcomFastBase, 
	 $HcomFastDbase, $HcomMonument, $HcomHaribote,
	 $HcomSchool, $HcomEste, $HcomTreaning, $HcomRest, $HcomPlay,
	 $HcomMissileNM, $HcomMissilePP, $HcomDoNothing,
	 $HcomMoney, $HcomFood, $HcomPropaganda, $HcomGiveup,
	 $HcomAutoPrepare, $HcomAutoPrepare2, $HcomAutoDelete);



# 計画の名前と値段
$HcomName[$HcomPrepare]		= '整地';
$HcomCost[$HcomPrepare]		= 1;
$HcomName[$HcomPrepare2]	= '地ならし';
$HcomCost[$HcomPrepare2]	= 30;
$HcomName[$HcomReclaim]		= '埋め立て';
$HcomCost[$HcomReclaim]		= 100;
$HcomName[$HcomDestroy]		= '掘削';
$HcomCost[$HcomDestroy]		= 300;
$HcomName[$HcomSellTree]	= '伐採';
$HcomCost[$HcomSellTree]	= 0;
$HcomName[$HcomPlant]		= '植林';
$HcomCost[$HcomPlant]		= 50;
$HcomName[$HcomFarm]		= '農場整備';
$HcomCost[$HcomFarm]		= 10;
$HcomName[$HcomFactory]		= '工場建設';
$HcomCost[$HcomFactory]		= 50;
$HcomName[$HcomMountain]	= '採掘場整備';
$HcomCost[$HcomMountain]	= 300;
$HcomName[$HcomBase]		= 'ミサイル基地建設';
$HcomName2[$HcomBase]		= 'ミサイル基地';
$HcomCost[$HcomBase]		= 200;
$HcomName[$HcomDbase]		= '防衛施設建設';
$HcomName2[$HcomDbase]		= '防衛施設';
$HcomCost[$HcomDbase]		= 500;
$HcomName[$HcomFastRec]		= '高速埋め立て';
$HcomName2[$HcomFastRec]	= '高速埋立';
$HcomCost[$HcomFastRec]		= 500;
$HcomName[$HcomFastDes]		= '高速掘削';
$HcomCost[$HcomFastDes]		= 1500;
$HcomName[$HcomFastPlant]	= '高速植林';
$HcomCost[$HcomFastPlant]	= 1000;
$HcomName[$HcomFastFarm]	= '高速農場整備';
$HcomName2[$HcomFastFarm]	= '高速農場';
$HcomCost[$HcomFastFarm]	= 500;
$HcomName[$HcomFastFact]	= '高速工場整備';
$HcomName2[$HcomFastFact]	= '高速工場';
$HcomCost[$HcomFastFact]	= 1000;
$HcomName[$HcomFastBase]	= '高速ミサイル基地建設';
$HcomName2[$HcomFastBase]	= '高速ミ基地';
$HcomCost[$HcomFastBase]	= 900;
$HcomName[$HcomFastDbase]	= '高速防衛施設建設';
$HcomName2[$HcomFastDbase]	= '高速防衛';
$HcomCost[$HcomFastDbase]	= 2000;
$HcomName[$HcomSbase]		= '海底基地建設';
$HcomCost[$HcomSbase]		= 999999;
$HcomName[$HcomMonument]	= '記念碑建造';
$HcomCost[$HcomMonument]	= 9999;
$HcomName[$HcomHaribote]	= 'ハリボテ設置';
$HcomCost[$HcomHaribote]	= 1;
$HcomName[$HcomSchool]		= 'いのら学校';
$HcomName2[$HcomSchool]		= '学校';
$HcomCost[$HcomSchool]		= 300;
$HcomName[$HcomEste]		= 'いのらエステ';
$HcomName2[$HcomEste]		= 'エステ';
$HcomCost[$HcomEste]		= 300;
$HcomName[$HcomTreaning]	= 'いのらジム';
$HcomName2[$HcomTreaning]	= 'ジム';
$HcomCost[$HcomTreaning]	= 800;
$HcomName[$HcomRest]		= 'いのら療養';
$HcomName2[$HcomRest]		= '療養';
$HcomCost[$HcomRest]		= 500;
$HcomName[$HcomPlay]		= 'いのら遊戯';
$HcomName2[$HcomPlay]		= '遊戯';
$HcomCost[$HcomPlay]		= 400;
$HcomName[$HcomMissileNM]	= 'ミサイル発射';
$HcomCost[$HcomMissileNM]	= 20;
$HcomName[$HcomMissilePP]	= 'PPミサイル発射';
$HcomCost[$HcomMissilePP]	= 40;
$HcomName[$HcomDoNothing]	= '資金繰り';
$HcomCost[$HcomDoNothing]	= 0;
$HcomName[$HcomSell]		= '食料輸出';
$HcomCost[$HcomSell]		= -100;
$HcomName[$HcomMoney]		= '資金援助';
$HcomCost[$HcomMoney]		= 100;
$HcomName[$HcomFood]		= '食料援助';
$HcomCost[$HcomFood]		= -100;
$HcomName[$HcomPropaganda]	= 'いのら大行進';
$HcomCost[$HcomPropaganda]	= 1000;
$HcomName[$HcomGiveup]		= '島の放棄';
$HcomCost[$HcomGiveup]		= 0;
$HcomName[$HcomAutoPrepare]	= '整地自動入力';
$HcomCost[$HcomAutoPrepare]	= 0;
$HcomName[$HcomAutoPrepare2]= '地ならし自動入力';
$HcomCost[$HcomAutoPrepare2]= 0;
$HcomName[$HcomAutoDelete]	= '全計画を白紙撤回';
$HcomCost[$HcomAutoDelete]	=  0;

#----------------------------------------------------------------------
# 変数
#----------------------------------------------------------------------

# COOKIE
my($defaultID);	   # 島の名前
my($defaultTarget);   # ターゲットの名前

# 島の座標数
$HpointNumber = $HislandSize * $HislandSize;

#----------------------------------------------------------------------
# メイン
#----------------------------------------------------------------------

# jcode.plをrequire
require($jcode);

if($Href) {
	my($page) = $ENV{'HTTP_REFERER'};
	$page =~ tr/+/ /;
	$page =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	if (!($page =~ /$ref_page/i)) { &access; }
}

sub access {
	print "Content-type: text/html\n\n";
	out (<<'END');
<HTML><HEAD><TITLE>アクセス禁止</TITLE></HEAD>
<BODY><BR><BR><center><H1>アクセス禁止</H1><br>
<font size=+1>トップページよりお入りください。<BR><br>
<A HREF=$ref_main>$ref_main</A>
</font>
</BODY></HTML>
END
	exit;
}

# 「戻る」リンク
$HtempBack = "<A HREF=\"$HthisFile\">${HtagBig_}トップへ戻る${H_tagBig}</A>";
$BODY = "<BODY $htmlBody>";

# ロックをかける
if(!hakolock()) {
	# ロック失敗
	# ヘッダ出力
	tempHeader();

	# ロック失敗メッセージ
	tempLockFail();

	# フッタ出力
	tempFooter();

	# 終了
	exit(0);
}

# 乱数の初期化
srand(time^$$);

# COOKIE読みこみ
cookieInput();

# CGI読みこみ
cgiInput();

# 島データの読みこみ
if(readIslandsFile($HcurrentID) == 0) {
	unlock();
	tempHeader();
	tempNoDataFile();
	tempFooter();
	exit(0);
}

# テンプレートを初期化
tempInitialize();

# COOKIE出力
cookieOutput();

# ヘッダ出力
if($HmainMode eq 'owner' && $HjavaMode eq 'java' ||
   $HmainMode eq 'commandJava' || # コマンド入力モード
   $HmainMode eq 'comment' && $HjavaMode eq 'java' || #コメント入力モード
   $HmainMode eq 'lbbs' && $HjavaMode eq 'java') { #コメント入力モード
	$BODY = "<BODY onload=\"init()\" $htmlBody>";
	require('hako-js.cgi');
	require('hako-map.cgi');
	# ヘッダ出力
	tempHeader();
	if($HmainMode eq 'commandJava') {
		# 開発モード
		commandJavaMain();
	} elsif($HmainMode eq 'comment') {
		# コメント入力モード
		commentMain();
	} elsif($HmainMode eq 'lbbs') {
		# ローカル掲示板モード
		localBbsMain();
	}else{
		ownerMain();
	}
	# フッタ出力
	tempFooter();
	# 終了
	exit(0);
}else{
	# ヘッダ出力
	tempHeader();
}

if($HmainMode eq 'turn') {
	# ターン進行
	require('hako-turn.cgi');
	require('hako-top.cgi');
	turnMain();

} elsif($HmainMode eq 'new') {
	# 島の新規作成
	require('hako-turn.cgi');
	require('hako-map.cgi');
	newIslandMain();

} elsif($HmainMode eq 'print') {
	# 観光モード
	require('hako-map.cgi');
	printIslandMain();

} elsif($HmainMode eq 'owner') {

	# 開発モード
	require('hako-map.cgi');
	ownerMain();

} elsif($HmainMode eq 'command') {
	# コマンド入力モード
	require('hako-map.cgi');
	commandMain();

} elsif($HmainMode eq 'comment') {
	# コメント入力モード
	require('hako-map.cgi');
	commentMain();

} elsif($HmainMode eq 'lbbs') {

	# ローカル掲示板モード
	require('hako-map.cgi');
	localBbsMain();

} elsif($HmainMode eq 'change') {
	# 情報変更モード
	require('hako-turn.cgi');
	require('hako-top.cgi');
	changeMain();

} elsif($HmainMode eq 'logView') {
	# LOGモード
	require('hako-top.cgi');
	logViewMain();

} else {
	# その他の場合はトップページモード
	require('hako-top.cgi');
	topPageMain();
}

# フッタ出力
tempFooter();

# 終了
exit(0);

# コマンドを前にずらす
sub slideFront {
	my($command, $number) = @_;
	my($i);

	# それぞれずらす
	splice(@$command, $number, 1);

	# 最後に資金繰り
	$command->[$HcommandMax - 1] = {
		'kind' => $HcomDoNothing,
		'target' => 0,
		'x' => 0,
		'y' => 0,
		'arg' => 0
		};
}

# コマンドを後にずらす
sub slideBack {
	my($command, $number) = @_;
	my($i);

	# それぞれずらす
	return if $number == $#$command;
	pop(@$command);
	splice(@$command, $number, 0, $command->[$number]);
}

#----------------------------------------------------------------------
# 島データ入出力
#----------------------------------------------------------------------

# 全島データ読みこみ
sub readIslandsFile {
	my($num) = @_; # 0だと地形読みこまず
				   # -1だと全地形を読む
				   # 番号だとその島の地形だけは読みこむ

	# データファイルを開く
	if(!open(IN, "${HdirName}/hakojima.dat")) {
		rename("${HdirName}/hakojima.tmp", "${HdirName}/hakojima.dat");
		if(!open(IN, "${HdirName}/hakojima.dat")) {
			return 0;
		}
	}

	# 各パラメータの読みこみ
	$HislandTurn	 = int(<IN>); # ターン数
	if($HislandTurn == 0) {
		return 0;
	}
	$HislandLastTime = int(<IN>); # 最終更新時間
	if($HislandLastTime == 0) {
		return 0;
	}
	$HislandNumber   = int(<IN>); # 島の総数
	$HislandNextID   = int(<IN>); # 次に割り当てるID

	# ターン処理判定
	my($now) = time;
	if((($Hdebug == 1) && 
		($HmainMode eq 'Hdebugturn')) ||
	   (($now - $HislandLastTime) >= $HunitTime)) {
		if($HislandLastTurn > $HislandTurn) {
			$turnMode = "debug" if($HmainMode eq 'Hdebugturn');
			$HmainMode = 'turn';
			$num = -1; # 全島読みこむ
		}
	}

	# 島の読みこみ
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		 $Hislands[$i] = readIsland($num);
		 $HidToNumber{$Hislands[$i]->{'id'}} = $i;
	}

	# ファイルを閉じる
	close(IN);

	return 1;
}

# 島ひとつ読みこみ
sub readIsland {
	my($num) = @_;
	my($name, $id, $prize, $absent, $comment, $password, $money, $food,
	   $pop, $area, $farm, $factory, $mountain, $score, $fire, $ownername);
	my($i_name, $i_cont, $i_gene, $i_age, $i_type, $i_ang, $i_heal,
		 $i_hp, $i_cute, $i_arm, $i_int, $i_sleep);

	$name = <IN>; # 島の名前
	chomp($name);
	if($name =~ s/,(.*)$//g) {
		$score = int($1);
	} else {
		$score = 0;
	}
	$id = int(<IN>);		# ID番号
	$prize = <IN>;			# 受賞
	chomp($prize);
	$absent = int(<IN>);	# 連続資金繰り数
	$comment = <IN>;		# コメント
	chomp($comment);
	$password = <IN>;		# 暗号化パスワード
	chomp($password);
	$money = int(<IN>);		# 資金
	$food = int(<IN>);		# 食料
	$pop = int(<IN>);		# 人口
	$area = int(<IN>);		# 広さ
	$farm = int(<IN>);		# 農場
	$factory = int(<IN>);	# 工場
	$mountain = int(<IN>);	# 採掘場
	$fire = int(<IN>);		# ミサイル発射数
	$ownername = <IN>;		# オーナーネーム
	chomp($ownername);
	$i_name = <IN>;			# いのらの名前
	chomp($i_name);
	$i_cont = <IN>;			# いのらコンテスト受賞数
	chomp($i_cont);
	$i_gene = int(<IN>);	# いのらの世代
	$i_age = int(<IN>);		# いのらの年
	$i_type = int(<IN>);	# いのらの種類
	$i_ang = int(<IN>);		# いのらの機嫌
	$i_heal = int(<IN>);	# いのらの健康度
	$i_hp = int(<IN>);		# いのらの体力
	$i_cute = int(<IN>);	# いのらの魅力
	$i_arm = int(<IN>);		# いのらの腕力
	$i_int = int(<IN>);		# いのらの知力
	$i_sleep = int(<IN>);	# いのら睡眠フラグ


	# HidToNameテーブルへ保存
	$HidToName{$id} = $name;		# 

	# 地形
	my(@land, @landValue, $line, @command, @lbbs);

	if(($num == -1) || ($num == $id)) {
		if(!open(IIN, "${HdirName}/island.$id")) {
			rename("${HdirName}/islandtmp.$id", "${HdirName}/island.$id");
			if(!open(IIN, "${HdirName}/island.$id")) {
				exit(0);
			}
		}
		my($x, $y);
		for($y = 0; $y < $HislandSize; $y++) {
			$line = <IIN>;
			for($x = 0; $x < $HislandSize; $x++) {
				$line =~ s/^(.)(..)//;
				$land[$x][$y] = hex($1);
				$landValue[$x][$y] = hex($2);
			}
		}

		# コマンド
		my($i);
		for($i = 0; $i < $HcommandMax; $i++) {
			$line = <IIN>;
			$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),([0-9]*)$/;
			$command[$i] = {
				'kind' => int($1),
				'target' => int($2),
				'x' => int($3),
				'y' => int($4),
				'arg' => int($5)
				}
		}

		# ローカル掲示板
		for($i = 0; $i < $HlbbsMax; $i++) {
			$line = <IIN>;
			chomp($line);
			$lbbs[$i] = $line;
		}

		close(IIN);
	}

	# 島型にして返す
	return {
		 'name' => $name,
		 'id' => $id,
		 'score' => $score,
		 'prize' => $prize,
		 'absent' => $absent,
		 'comment' => $comment,
		 'password' => $password,
		 'money' => $money,
		 'food' => $food,
		 'pop' => $pop,
		 'area' => $area,
		 'farm' => $farm,
		 'factory' => $factory,
		 'mountain' => $mountain,
		 'fire' => $fire,
		 'ownername' => $ownername,
		 'i_name' => $i_name,
		 'i_cont' => $i_cont,
		 'i_gene' => $i_gene,
		 'i_age'  => $i_age,
		 'i_type' => $i_type,
		 'i_ang'  => $i_ang,
		 'i_heal' => $i_heal,
		 'i_hp'   => $i_hp,
		 'i_cute' => $i_cute,
		 'i_arm'  => $i_arm,
		 'i_int'  => $i_int,
		 'i_sleep'  => $i_sleep,
		 'land' => \@land,
		 'landValue' => \@landValue,
		 'command' => \@command,
		 'lbbs' => \@lbbs,
	};
}

# 全島データ書き込み
sub writeIslandsFile {
	my($num) = @_;

	# ファイルを開く
	open(OUT, ">${HdirName}/hakojima.tmp");

	# 各パラメータ書き込み
	print OUT "$HislandTurn\n";
	print OUT "$HislandLastTime\n";
	print OUT "$HislandNumber\n";
	print OUT "$HislandNextID\n";

	# 島の書きこみ
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		 writeIsland($Hislands[$i], $num);
	}

	# ファイルを閉じる
	close(OUT);

	# 本来の名前にする
	unlink("${HdirName}/hakojima.dat");
	rename("${HdirName}/hakojima.tmp", "${HdirName}/hakojima.dat");
}

# 島ひとつ書き込み
sub writeIsland {
	my($island, $num) = @_;
	my($score);
	$score = int($island->{'score'});
	print OUT $island->{'name'} . ",$score\n";
	print OUT $island->{'id'} . "\n";
	print OUT $island->{'prize'} . "\n";
	print OUT $island->{'absent'} . "\n";
	print OUT $island->{'comment'} . "\n";
	print OUT $island->{'password'} . "\n";
	print OUT $island->{'money'} . "\n";
	print OUT $island->{'food'} . "\n";
	print OUT $island->{'pop'} . "\n";
	print OUT $island->{'area'} . "\n";
	print OUT $island->{'farm'} . "\n";
	print OUT $island->{'factory'} . "\n";
	print OUT $island->{'mountain'} . "\n";
	print OUT $island->{'fire'} . "\n";
	print OUT $island->{'ownername'} . "\n";
	print OUT $island->{'i_name'} . "\n";
	print OUT $island->{'i_cont'} . "\n";
	print OUT $island->{'i_gene'} . "\n";
	print OUT $island->{'i_age'} . "\n";
	print OUT $island->{'i_type'} . "\n";
	print OUT $island->{'i_ang'} . "\n";
	print OUT $island->{'i_heal'} . "\n";
	print OUT $island->{'i_hp'} . "\n";
	print OUT $island->{'i_cute'} . "\n";
	print OUT $island->{'i_arm'} . "\n";
	print OUT $island->{'i_int'} . "\n";
	print OUT $island->{'i_sleep'} . "\n";

	# 地形
	if(($num <= -1) || ($num == $island->{'id'})) {
		open(IOUT, ">${HdirName}/islandtmp.$island->{'id'}");

		my($land, $landValue);
		$land = $island->{'land'};
		$landValue = $island->{'landValue'};
		my($x, $y);
		for($y = 0; $y < $HislandSize; $y++) {
			for($x = 0; $x < $HislandSize; $x++) {
				printf IOUT ("%x%02x", $land->[$x][$y], $landValue->[$x][$y]);
			}
			print IOUT "\n";
		}

		# コマンド
		my($command, $cur, $i);
		$command = $island->{'command'};
		for($i = 0; $i < $HcommandMax; $i++) {
			printf IOUT ("%d,%d,%d,%d,%d\n", 
						 $command->[$i]->{'kind'},
						 $command->[$i]->{'target'},
						 $command->[$i]->{'x'},
						 $command->[$i]->{'y'},
						 $command->[$i]->{'arg'}
						 );
		}

		# ローカル掲示板
		my($lbbs);
		$lbbs = $island->{'lbbs'};
		for($i = 0; $i < $HlbbsMax; $i++) {
			print IOUT $lbbs->[$i] . "\n";
		}

		close(IOUT);
		unlink("${HdirName}/island.$island->{'id'}");
		rename("${HdirName}/islandtmp.$island->{'id'}", "${HdirName}/island.$island->{'id'}");
	}
}

#----------------------------------------------------------------------
# 入出力
#----------------------------------------------------------------------

# 標準出力への出力
sub out {
	print STDOUT jcode::sjis($_[0]);
}

# デバッグログ
sub HdebugOut {
   open(DOUT, ">>debug.log");
   print DOUT ($_[0]);
   close(DOUT);
}

# CGIの読みこみ
sub cgiInput {
	my($line, $getLine);

	# 入力を受け取って日本語コードをEUCに
	$line = <>;
	$line =~ tr/+/ /;
	$line =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$line = jcode::euc($line);
	$line =~ s/[\x00-\x1f\,]//g;

	# GETのやつも受け取る
	$getLine = $ENV{'QUERY_STRING'};

	# 対象の島
	if($line =~ /CommandButton([0-9]+)=/) {
		# コマンド送信ボタンの場合
		$HcurrentID = $1;
		$defaultID = $1;
	}

	if($line =~ /ISLANDNAME=([^\&]*)\&/){
		# 名前指定の場合
		$HcurrentName = cutColumn($1, 32);
	}
	if($line =~ /MONSTERNAME=([^\&]*)\&/){
		# 名前指定の場合
		$Hi_name = cutColumn($1, 32);
	}

	if($line =~ /ISLANDID=([0-9]+)\&/){
		# その他の場合
		$HcurrentID = $1;
		$defaultID = $1;
	}

	# パスワード
	if($line =~ /OLDPASS=([^\&]*)\&/) {
		$HoldPassword = $1;
		$HdefaultPassword = $1;
	}
	if($line =~ /PASSWORD=([^\&]*)\&/) {
		$HinputPassword = $1;
		$HdefaultPassword = $1;
	}
	if($line =~ /PASSWORD2=([^\&]*)\&/) {
		$HinputPassword2 = $1;
	}

	# メッセージ
	if($line =~ /MESSAGE=([^\&]*)\&/) {
		$Hmessage = cutColumn($1, 80);
	}

	# ローカル掲示板
	if($line =~ /LBBSNAME=([^\&]*)\&/) {
		$HlbbsName = $1;
		$HdefaultName = $1;
	}
	if($line =~ /LBBSMESSAGE=([^\&]*)\&/) {
		$HlbbsMessage = cutColumn($1, 80);
	}

	if($line =~ /IMGLINEMAC=([^&]*)\&/){
		my($flag) = 'file:///' . $1;
		$HimgLine = $flag;
	}

	if($line =~ /IMGLINE=([^&]*)\&/){
		my($flag) = substr($1, 0 , -10);
		$flag =~ tr/\\/\//;
		if($flag eq 'del'){ $flag = $imageDir; } else { $flag = 'file:///' . $flag; }
		$HimgLine = $flag;
	}

	if($line =~ /OWNERNAME=([^\&]*)\&/){
		# オーナー名指定の場合
		$HownerName = cutColumn($1, 22);
	}
	# Ｊａｖａスクリプトモード
	if($line =~ /JAVAMODE=(cgi|java)/) {
		$HjavaMode = $1;
	}

	# 非同期通信フラグ
	if($line =~ /async=true\&/) {
		$Hasync = 1;
	}

	if($line =~ /CommandJavaButton([0-9]+)=/) {
		# コマンド送信ボタンの場合（Ｊａｖａスクリプト）
		$HcurrentID = $1;
		$defaultID = $1;
	}
	# main modeの取得
	if($line =~ /TurnButton/) {
		if($Hdebug == 1) {
			$HmainMode = 'Hdebugturn';
		}
	} elsif($line =~ /OwnerButton/) {
		$HmainMode = 'owner';
	} elsif($getLine =~ /Sight=([0-9]*)/) {
		$HmainMode = 'print';
		$HcurrentID = $1;
	} elsif($line =~ /ChangeOwnerName/) {
		$HmainMode = 'change';
	} elsif($getLine =~ /LogFileView=([0-9]*)/) {
		$HmainMode = 'logView';
		$Hlogturn = ($1 > $HlogMax) ? $HlogMax : $1;
	} elsif($line =~ /NewIslandButton/) {
		$HmainMode = 'new';
	} elsif($line =~ /LbbsButton(..)([0-9]*)/) {
		$HmainMode = 'lbbs';
		if($1 eq 'FO') {
			# 観光者
			$HlbbsMode = 0;
			$HforID = $HcurrentID;
		} elsif($1 eq 'OW') {
			# 島主
			$HlbbsMode = 1;
		} else {
			# 削除
			$HlbbsMode = 2;
		}
		$HcurrentID = $2;

		# 削除かもしれないので、番号を取得
		$line =~ /NUMBER=([^\&]*)\&/;
		$HcommandPlanNumber = $1;

	} elsif($line =~ /ChangeInfoButton/) {
		$HmainMode = 'change';
	} elsif($line =~ /MessageButton([0-9]*)/) {
		$HmainMode = 'comment';
		$HcurrentID = $1;
	} elsif($line =~ /CommandJavaButton/) {
		$HmainMode = 'commandJava';
		$line =~ /COMARY=([^\&]*)\&/;
		$HcommandComary = $1;
	} elsif($line =~ /CommandButton/) {
		$HmainMode = 'command';

		# コマンドモードの場合、コマンドの取得
		$line =~ /NUMBER=([^\&]*)\&/;
		$HcommandPlanNumber = $1;
		$line =~ /COMMAND=([^\&]*)\&/;
		$HcommandKind = $1;
		$HdefaultKind = $1;
		$line =~ /AMOUNT=([^\&]*)\&/;
		$HcommandArg = $1;
		$line =~ /TARGETID=([^\&]*)\&/;
		$HcommandTarget = $1;
		$defaultTarget = $1;
		$line =~ /POINTX=([^\&]*)\&/;
		$HcommandX = $1;
		$HdefaultX = $1;
		$line =~ /POINTY=([^\&]*)\&/;
		$HcommandY = $1;
		$HdefaultY = $1;
		$line =~ /COMMANDMODE=(write|insert|delete)/;
		$HcommandMode = $1;

	} else {
		$HmainMode = 'top';
	}

}


#cookie入力
sub cookieInput {
	my($cookie);

	$cookie = jcode::euc($ENV{'HTTP_COOKIE'});

	if($cookie =~ /${HthisFile}OWNISLANDID=\(([^\)]*)\)/) {
		$defaultID = $1;
	}
	if($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
		$HdefaultPassword = $1;
	}
	if($cookie =~ /${HthisFile}LBBSNAME=\(([^\)]*)\)/) {
		$HdefaultName = $1;
	}
	if($cookie =~ /${HthisFile}POINTX=\(([^\)]*)\)/) {
		$HdefaultX = $1;
	}
	if($cookie =~ /${HthisFile}POINTY=\(([^\)]*)\)/) {
		$HdefaultY = $1;
	}
	if($cookie =~ /${HthisFile}KIND=\(([^\)]*)\)/) {
		$HdefaultKind = $1;
	}
	if($cookie =~ /${HthisFile}IMGLINE=\(([^\)]*)\)/) {
		$HimgLine = $1;
	}
	if($cookie =~ /${HthisFile}JAVAMODE=\(([^\)]*)\)/) {
		$makeMode = $1;
	}

}

#cookie出力
sub cookieOutput {
	my($cookie, $info);

	# 消える期限の設定
	my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) =
		gmtime(time + 30 * 86400); # 現在 + 30日

	# 2ケタ化
	$year += 1900;
	if ($date < 10) { $date = "0$date"; }
	if ($hour < 10) { $hour = "0$hour"; }
	if ($min < 10) { $min  = "0$min"; }
	if ($sec < 10) { $sec  = "0$sec"; }

	# 曜日を文字に
	$day = ("Sunday", "Monday", "Tuesday", "Wednesday",
			"Thursday", "Friday", "Saturday")[$day];

	# 月を文字に
	$mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
			"Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

	# パスと期限のセット
	$info = "; expires=$day, $date\-$mon\-$year $hour:$min:$sec GMT\n";
	$cookie = '';
	
	if(($HcurrentID) && ($HmainMode eq 'owner')){
		$cookie .= "Set-Cookie: ${HthisFile}OWNISLANDID=($HcurrentID) $info";
	}
	if($HinputPassword) {
		$cookie .= "Set-Cookie: ${HthisFile}OWNISLANDPASSWORD=($HinputPassword) $info";
	}
	if($HlbbsName) {
		$cookie .= "Set-Cookie: ${HthisFile}LBBSNAME=($HlbbsName) $info";
	}
	if($HcommandX) {
		$cookie .= "Set-Cookie: ${HthisFile}POINTX=($HcommandX) $info";
	}
	if($HcommandY) {
		$cookie .= "Set-Cookie: ${HthisFile}POINTY=($HcommandY) $info";
	}
	if($HcommandKind) {
		# 自動系以外
		$cookie .= "Set-Cookie: ${HthisFile}KIND=($HcommandKind) $info";
	}
	if($HimgLine) {
		$cookie .= "Set-Cookie: ${HthisFile}IMGLINE=($HimgLine) $info";
	}
	if($HjavaMode) {
		$cookie .= "Set-Cookie: ${HthisFile}JAVAMODE=($HjavaMode) $info";
	}
	out($cookie);
}

#----------------------------------------------------------------------
# ユーティリティ
#----------------------------------------------------------------------
sub hakolock {
	# ロックを試す
	$lfh = file_lock() or die return 0;
	return 1;
}

# ロックを外す
sub unlock {
	# rename式ロック
	rename($lfh->{current}, $lfh->{path});
}

# 新ロック方式
sub file_lock {
	my %lfh = (dir => "./", basename => "lock/lockfile", timeout => $unlockTime, trytime => 3, @_);
	$lfh{path} = $lfh{dir}.$lfh{basename};

	for (my $i = 0; $i < $lfh{trytime}; $i++, sleep 1) {
		return \%lfh if (rename($lfh{path}, $lfh{current} = $lfh{path} . time));
	}

	opendir(LOCKDIR, $lfh{dir});
	my @filelist = readdir(LOCKDIR);
	closedir(LOCKDIR);

	foreach (@filelist) {
		if (/^lockfile(\d+)/) {
			return \%lfh if (time - $1 > $lfh{timeout} and
			rename($lfh{dir} . $_, $lfh{current} = $lfh{path} . time));
			last;
		}
	}
	undef;
}

# 小さい方を返す
sub min {
	return ($_[0] < $_[1]) ? $_[0] : $_[1];
}

# パスワードエンコード
sub encode {
	if($cryptOn == 1) {
		return crypt($_[0], 'h2');
	} else {
		return $_[0];
	}
}

# パスワードチェック
sub checkPassword {
	my($p1, $p2) = @_;

	# nullチェック
	if($p2 eq '') {
		return 0;
	}

	# マスターパスワードチェック
	if($masterPassword eq $p2) {
		return 1;
	}

	# 本来のチェック
	if($p1 eq encode($p2)) {
		return 1;
	}

	return 0;
}

# 1000億単位丸めルーチン
sub aboutMoney {
	my($m) = @_;
	if($m < 500) {
		return "推定500${HunitMoney}未満";
	} else {
		$m = int(($m + 500) / 1000);
		return "推定${m}000${HunitMoney}";
	}
}

# エスケープ文字の処理
sub htmlEscape {
	my($s) = @_;
	$s =~ s/&/&amp;/g;
	$s =~ s/</&lt;/g;
	$s =~ s/>/&gt;/g;
	$s =~ s/\"/&quot;/g; #"
	return $s;
}

# 80ケタに切り揃え
sub cutColumn {
	my($s, $c) = @_;
	if(length($s) <= $c) {
		return $s;
	} else {
		# 合計80ケタになるまで切り取り
		my($ss) = '';
		my($count) = 0;
		while($count < $c) {
			$s =~ s/(^[\x80-\xFF][\x80-\xFF])|(^[\x00-\x7F])//;
			if($1) {
				$ss .= $1;
				$count ++;
			} else {
				$ss .= $2;
			}
			$count ++;
		}
		return $ss;
	}
}

# 島の名前から番号を得る(IDじゃなくて番号)
sub nameToNumber {
	my($name) = @_;

	# 全島から探す
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		if($Hislands[$i]->{'name'} eq $name) {
			return $i;
		}
	}

	# 見つからなかった場合
	return -1;
}

# 怪獣の情報
sub monsterSpec {
	my($lv,$island) = @_;

	# 種類
	my($kind) = int($lv / 10);

	# 名前
	my($name);
	$name = $HmonsterName[$kind];

	# 体力
	my($hp) = $lv - ($kind * 10);

	if($kind >= 4 and $island) {
		$kind = $island->{'i_type'};
		$hp = $island->{'i_hp'};
		$name = $island->{'i_name'};
	}

	return ($kind, $name, $hp);
}

# 経験地からレベルを算出
sub expToLevel {
	my($kind, $exp) = @_;
	my($i);
	if($kind == $HlandBase) {
		# ミサイル基地
		for($i = $maxBaseLevel; $i > 1; $i--) {
			if($exp >= $baseLevelUp[$i - 2]) {
				return $i;
			}
		}
		return 1;
	} else {
		# 海底基地
		for($i = $maxSBaseLevel; $i > 1; $i--) {
			if($exp >= $sBaseLevelUp[$i - 2]) {
				return $i;
			}
		}
		return 1;
	}

}

# (0,0)から(size - 1, size - 1)までの数字が一回づつ出てくるように
# (@Hrpx, @Hrpy)を設定
sub makeRandomPointArray {
	# 初期値
	my($y);
	@Hrpx = (0..$HislandSize-1) x $HislandSize;
	for($y = 0; $y < $HislandSize; $y++) {
		push(@Hrpy, ($y) x $HislandSize);
	}

	# シャッフル
	my ($i);
	for ($i = $HpointNumber; --$i; ) {
		my($j) = int(rand($i+1)); 
		if($i == $j) { next; }
		@Hrpx[$i,$j] = @Hrpx[$j,$i];
		@Hrpy[$i,$j] = @Hrpy[$j,$i];
	}
}

# 0から(n - 1)の乱数
sub random {
	return int(rand(1) * $_[0]);
}

#----------------------------------------------------------------------
# ログ表示
#----------------------------------------------------------------------
# ファイル番号指定でログ表示
sub logFilePrint {
	my($fileNumber, $id, $mode, $kankou) = @_;
	open(LIN, "${HdirName}/hakojima.log$_[0]");
	my($line, $m, $turn, $id1, $id2, $message);
	my($fi) = 0;

	while($line = <LIN>) {
		$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
		($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

		# 機密関係
		if($m == 1) {
			if(($mode == 0) || ($id1 != $id)) {
				# 機密表示権利なし
				next;
			}
			$m = '<B>(機密)</B>';
		} else {
			$m = '';
		}

		# 表示的確か
		if($id != 0) {
			if(($id != $id1) &&
			   ($id != $id2)) {
				next;
			}
		}

		# 表示
		if($kankou == 1) {

		out("<NOBR>${HtagNumber_}ターン$turn$m${H_tagNumber}：$message</NOBR><BR>\n");

	} elsif(($fi == 0) && ($mode == 0)) {
	 out("<NOBR><BR><B><I><FONT COLOR='#000000' SIZE=+2>ターン$turn$m：</FONT></I></B><BR><HR width=50% align=left>\n");
		out("<NOBR>${HtagNumber_}ターン$turn$m${H_tagNumber}：$message</NOBR><BR>\n");
		  $fi++;
		} else {
		out("<NOBR>${HtagNumber_}ターン$turn$m${H_tagNumber}：$message</NOBR><BR>\n");
		}
	}
#		out("<hr>\n");
	close(LIN);
}

#----------------------------------------------------------------------
# テンプレート
#----------------------------------------------------------------------
# 初期化
sub tempInitialize {
	# 島セレクト(デフォルト自分)
	$HislandList = getIslandList($defaultID);
	$HtargetList = getIslandList($defaultID);
}

# 島データのプルダウンメニュー用
sub getIslandList {
	my($select) = @_;
	my($list, $name, $id, $s, $i);

	#島リストのメニュー
	$list = '';
	for($i = 0; $i < $HislandNumber; $i++) {
		$name = $Hislands[$i]->{'name'};
		$id = $Hislands[$i]->{'id'};
		if($id eq $select) {
			$s = 'SELECTED';
		} else {
			$s = '';
		}
		$list .=
			"<OPTION VALUE=\"$id\" $s>${name}島\n";
	}
	return $list;
}

# ロック失敗
sub tempLockFail {
	# タイトル
	out(<<END);
${HtagBig_}同時アクセスエラーです。<BR>
ブラウザの「戻る」ボタンを押し、<BR>
しばらく待ってから再度お試し下さい。${H_tagBig}$HtempBack
END
}

# 強制解除
sub tempUnlock {
	# タイトル
	out(<<END);
${HtagBig_}前回のアクセスが異常終了だったようです。<BR>
ロックを強制解除しました。${H_tagBig}$HtempBack
END
}

# hakojima.datがない
sub tempNoDataFile {
	out(<<END);
${HtagBig_}データファイルが開けません。${H_tagBig}$HtempBack
END
}

# パスワード間違い
sub tempWrongPassword {
	out(<<END);
${HtagBig_}パスワードが違います。${H_tagBig}$HtempBack
END
}

# 何か問題発生
sub tempProblem {
	out(<<END);
${HtagBig_}問題発生、とりあえず戻ってください。${H_tagBig}$HtempBack
END
}

# 時間取得
sub get_time {
	my $time_;
	my $TZ_JST=3600*9;
	my($sec,$min,$hour,$mday,$mon,$year)=gmtime($_[0]+$TZ_JST);
	my $now=time();
	my($nsec,$nmin,$nhour,$nmday,$nmon,$nyear)=gmtime($now+$TZ_JST);
	if($_[0]<$now-12*3600 && ($nyear!=$year || $nmon!=$mon || $nmday!=$mday)) {
		$mon = ($mon < 9) ? "0".($mon+1) : $mon + 1;
		$mday = ($mday < 10) ? "0".$mday : $mday;
		$time_ = "(".$mon."/$mday)";
	} else {
		$hour = ($hour < 10) ? "0".$hour : $hour;
		$min = ($min < 10) ? "0".$min : $min;
		$time_ = "(<B>$hour:$min</B>)";
	}
	return $time_;
}
