#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# 設定ファイル
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# いのら諸島
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# 各種設定値
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# 以下、必ず設定する部分
#----------------------------------------------------------------------

# このファイルを置くディレクトリ
# $baseDir = 'http://サーバー/ディレクトリ';
#
# 例)
# http://cgi2.bekkoame.ne.jp/cgi-bin/user/u5534/hakoniwa/hako-main.cgi
# として置く場合、
# $baseDir = 'http://cgi2.bekkoame.ne.jp/cgi-bin/user/u5534/hakoniwa';
# とする。最後にスラッシュ(/)は付けない。

$baseDir = 'http://localhost/~inora';

# 画像ファイルを置くディレクトリ
# $imageDir = 'http://サーバ';
$imageDir = 'http://localhost/~inora/hako/hakopng';

# 画像のローカル設定の説明ページ
$imageExp = 'http://localhost/~inora/hako/imgexp';

# jcode.plの位置
# $jcode = '/usr/libperl/jcode.pl';  # ベッコアメの場合
# $jcode = './jcode.pl';			 # 同じディレクトリに置く場合
$jcode = './jcode.pl';

# マスターパスワード
# このパスワードは、すべての島のパスワードを代用できます。
# 例えば、「他の島のパスワード変更」等もできます。
$masterPassword = 'master';

# 特殊パスワード
# このパスワードで「名前変更」を行うと、その島の資金、食料が最大値になります。
# (実際に名前を変える必要はありません。)
$HspecialPassword = 'special';

# 管理者名
$adminName = '管理者';

# 管理者のメールアドレス
$email = '****@***.**.**';

# 掲示板の名称
$bbsname = 'いのら諸島掲示板';

# 掲示板アドレス
$bbs = 'http://localhost/~inora/bbs/petit.cgi';

# 掲示板のログファイル
$bbs_log = './bbs/petit.log';

# ホームページのアドレス
$toppage = 'http://localhost/~inora/';

# マニュアルのアドレス
$manual = 'http://localhost/~inora/man.html';

# ディレクトリのパーミッション
# 通常は0755でよいが、0777、0705、0704等でないとできないサーバーもあるらしい
$HdirMode = 0755;

# データディレクトリの名前
# ここで設定した名前のディレクトリ以下にデータが格納されます。
# デフォルトでは'data'となっていますが、セキュリティのため
# なるべく違う名前に変更してください。
$HdirName = 'data';

#----------------------------------------------------------------------
# 必ず設定する部分は以上
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# 以下、好みによって設定する部分
#----------------------------------------------------------------------
#----------------------------------------
# ゲームの進行やファイルなど
#----------------------------------------
# 1ターンが何秒か
$HunitTime = 14400; # 4時間

# 最終ターン
$HislandLastTurn = 500;

# 異常終了基準時間
# (ロック後何秒で、強制解除するか)
$unlockTime = 120;

# 島の最大数
$HmaxIsland = 30;

# トップページに表示するログのターン数
$HtopLogTurn = 1;

# ログファイル保持ターン数
$HlogMax = 8; 

# バックアップを何ターンおきに取るか
$HbackupTurn = 12;

# バックアップを何回分残すか
$HbackupTimes = 4;

# 発見ログ保持行数
$HhistoryMax = 10;

# 放棄コマンド自動入力ターン数
$HgiveupTurn = 28;

# コマンド入力限界数
# (ゲームが始まってから変更すると、データファイルの互換性が無くなります。)
$HcommandMax = 30;

# ローカル掲示板行数を使用するかどうか(0:使用しない、1:使用する)
$HuseLbbs = 1;

# ローカル掲示板行数
$HlbbsMax = 10;

# 島の大きさ
# (変更できないかも)
$HislandSize = 12;

# 他人から資金を見えなくするか
# 0 見えない
# 1 見える
# 2 100の位で四捨五入
$HhideMoneyMode = 2;

# パスワードの暗号化(0だと暗号化しない、1だと暗号化する)
$cryptOn = 1;

# デバッグモード(1だと、「ターンを進める」ボタンが使用できる)
$Hdebug = 0;

# ---------------------------------------------------------------- 
# 不正アクセス禁止用設定
# 他サーバーからの箱庭スクリプトへの直リンクを禁止する設定です
# これを使用すると、レンタル掲示板等を利用している場合は、そこからの直リンクも出来なくなってしまいます
# これを読んでよくわからない方は、設定しない方が無難です
# 
# 1の場合は他サイトからのアクセス禁止
# 0なら、使用しない・・・
$Href = 0;

# 箱庭設置ページ
# 設置サイトのＵＲＬが　http://www.hakoniwa.com/~gabacho/hako/hako-main.cgi
# だったら、http://www.hakoniwa.com/~gabacho/　となります

$ref_page = 'http://localhost/';

# 箱庭トップページ
# 不正アクセスがあった場合のリンク先
# 大体の場合は、上記と同じになります

$ref_main = 'http://localhost/';

# ---------------------------------------------------------------- 

#----------------------------------------
# 資金、食料などの設定値と単位
#----------------------------------------
# 初期資金
$HinitialMoney = 1000;

# 初期食料
$HinitialFood = 3000;

# お金の単位
$HunitMoney = '億円';

# 食料の単位
$HunitFood = '00トン';

# 人口の単位
$HunitPop = '00人';

# 広さの単位
$HunitArea = '00万坪';

# 木の数の単位
$HunitTree = '00本';

# 木の単位当たりの売値
$HtreeValue = 5;

# １ターンで木の増える本数
$HtreeUp = 1;

# 名前変更のコスト
$HcostChangeName = 0;

# 人口1単位あたりの食料消費料
$HeatenFood = 0.2;

#----------------------------------------
# 基地の経験値
#----------------------------------------
# 経験値の最大値
$HmaxExpPoint = 200; # ただし、最大でも255まで

# レベルの最大値
$maxBaseLevel = 5;  # ミサイル基地
$maxSBaseLevel = 3; # 海底基地

# 経験値がいくつでレベルアップか
@baseLevelUp, @sBaseLevelUp;
@baseLevelUp = (20, 60, 120, 200); # ミサイル基地
@sBaseLevelUp = (50, 200);		 # 海底基地

#----------------------------------------
# 防衛施設の自爆
#----------------------------------------
# 怪獣に踏まれた時自爆するなら1、しないなら0
$HdBaseAuto = 0;

#----------------------------------------
# 災害
#----------------------------------------
# 通常災害発生率(確率は0.1%単位)
$HdisEarthquake	= 3;  # 地震
$HdisTsunami	= 10; # 津波
$HdisTyphoon	= 15; # 台風
$HdisMeteo		= 15; # 隕石
$HdisHugeMeteo	= 0;  # 巨大隕石
$HdisEruption	= 10; # 噴火
$HdisFire		= 5;  # 火災
$HdisMaizo		= 20; # 埋蔵金
$HdisVirus		= 200;# いのら病気
$HdisTyphIno	= 300;# いのら台風で飛ぶ

# いのらの病気
$VIRUS[0]	= '風邪をひいて';
$VIRUS[1]	= '伝染病にかかり';
$VIRUS[2]	= '盲腸になり';
$VIRUS[3]	= '頭痛がひどくて';
$VIRUS[4]	= '腹痛がひどくて';

# 地盤沈下
$HdisFallBorder = 200; # 安全限界の広さ(Hex数)
$HdisFalldown   = 0; # その広さを超えた場合の確率

# 怪獣
$HdisMonsBorder1 = 2000; # 人口基準1(怪獣レベル1)
$HdisMonsBorder2 = 3000; # 人口基準2(怪獣レベル2)
$HdisMonsBorder3 = 4000; # 人口基準3(怪獣レベル3)
$HdisMonster	 = 2;	 # 単位面積あたりの出現率(0.01%単位)

# 種類
$HmonsterNumber  = 4;

# 各基準において出てくる怪獣の番号の最大値
$HmonsterLevel1  = 1; # サンジラまで
$HmonsterLevel2  = 2; # いのらゴーストまで
$HmonsterLevel3  = 3; # キングいのらまで(全部)

# 名前
@HmonsterName = 
	(
	 'メカいのら',			# 0(人造)
	 '怪獣サンジラ',		# 1
	 '怪獣いのらゴースト',	# 2
	 '怪獣クジラ',			# 3
	 'ベビーいのら',		# 4
	 '肥満いのら',			# 5
	 'グリーンいのら',		# 6
	 'レッドいのら',		# 7
	 'ダークいのら',		# 8
	 'キングいのら',		# 9
	 'クィーンいのら',		# 10
	 'グレいのら'			# 11
);

# 最低体力、体力の幅、特殊能力、経験値、死体の値段
@HmonsterBHP	 = ( 2, 1, 1, 4,  1, 1, 1, 1);
@HmonsterDHP	 = ( 0, 2, 0, 2,  0, 0, 0, 0);
@HmonsterSpecial = ( 0, 3, 2, 4,  2, 0, 0, 0, 1);
@HmonsterExp	 = ( 5, 7, 10,20);
@HmonsterValue   = ( 0, 500, 300, 1500);

# 特殊能力の内容は、
# 0 特になし
# 1 足が速い(最大2歩あるく)
# 2 足がとても速い(最大何歩あるくか不明)
# 3 奇数ターンは硬化
# 4 偶数ターンは硬化
# 5 良く眠る
# 6 すぐ怒る

# 画像ファイル
$HmonsterImage[0]	= 'monster0.png';
$HmonsterImage[1]	= 'monster1.png';
$HmonsterImage[2]	= 'monster2.png';
$HmonsterImage[3]	= 'monster3.png';
$HmonsterImage[4]	= 'monster5.png';
$HmonsterImage[5]	= 'monster6.png';
$HmonsterImage[6]	= 'monster7.png';
$HmonsterImage[7]	= 'monster8.png';
$HmonsterImage[8]	= 'monster9.png';
$HmonsterImage[9]	= 'monster10.png';
$HmonsterImage[10]	= 'monster11.png';
$HmonsterImage[11]	= 'monster6.png';


# 画像ファイルその2(硬化中)
@HmonsterImage2 =
	('', 'monster4.png', '', 'monster4.png');

# いのら成長度合い
$INORA[0] = 100;
$INORA[1] = 200;
$INORA[2] = 400;

# 食料消費率修正（1で体力と同数）
$FOOD[4]  = 5;  # ベビーいのら
$FOOD[5]  = 20; # 肥満いのら
$FOOD[6]  = 10; # グリーンいのら
$FOOD[7]  = 10; # レッドいのら
$FOOD[8]  = 10; # ダークいのら
$FOOD[9]  = 15; # キングいのら
$FOOD[10] = 12; # クィーンいのら
$FOOD[11] = 8;  # グレいのら

# 基本睡眠ターン数
$SLEEP[4]  = 6; # ベビーいのら
$SLEEP[5]  = 7; # 肥満いのら
$SLEEP[6]  = 3; # グリーンいのら
$SLEEP[7]  = 3; # レッドいのら
$SLEEP[8]  = 3; # ダークいのら
$SLEEP[9]  = 4; # キングいのら
$SLEEP[10] = 4; # クィーンいのら
$SLEEP[11] = 2; # グレいのら

# 基本行動ターン数（つまり起きてる時間）
$WAKE[4]  = 4; # ベビーいのら
$WAKE[5]  = 3; # 肥満いのら
$WAKE[6]  = 7; # グリーンいのら
$WAKE[7]  = 7; # レッドいのら
$WAKE[8]  = 7; # ダークいのら
$WAKE[9]  = 6; # キングいのら
$WAKE[10] = 6; # クィーンいのら
$WAKE[11] = 8; # グレいのら

# コマンドによる成長の種別修正値
@rebi_def	= (50, 100, 300, 0);
@rebi_ang	= (0,0,0,0, 0, 0, 1, 1, 1, 2, 0, 3);
@rebi_heal	= (0,0,0,0, 0, 0, 2, 2, 2, 1, 0, 3);
@rebi_hp	= (0,0,0,0, 1, 2, 1, 1, 1, 1, 0, 0);
@rebi_arm	= (0,0,0,0, 1, 1, 2, 1, 0, 1, 0, 2);
@rebi_cute	= (0,0,0,0, 1, 1, 0, 2, 1, 1, 0, 0);
@rebi_int	= (0,0,0,0, 1, 1, 1, 0, 2, 1, 0, 0);

# イベント（0.1%）
$HinoraEventQuake = 250;  # 機嫌悪くて地震

#----------------------------------------
# 油田
#----------------------------------------
# 油田の収入
$HoilMoney = 1000;

# 油田の枯渇確率
$HoilRatio = 40;

#----------------------------------------
# 記念碑
#----------------------------------------
# 何種類あるか
$HmonumentNumber = 4;

# 名前
@HmonumentName = 
	(
	 'モノリス', 
	 '平和記念碑', 
	 '戦いの碑',
	 'いのら記念碑'
	);

# 画像ファイル
@HmonumentImage = 
	(
	 'monument0.png',
	 'monument0.png',
	 'monument0.png',
	 'monument1.png'
	 );


#----------------------------------------
# 賞関係
#----------------------------------------

$HturnPrizeUnit	= 100; # ターン杯を何ターン毎に出すか

# 賞の名前
$Hprize[0] = 'ターン杯';
$Hprize[1] = '繁栄賞';
$Hprize[2] = '超繁栄賞';
$Hprize[3] = '究極繁栄賞';
$Hprize[4] = '平和賞';
$Hprize[5] = '超平和賞';
$Hprize[6] = '究極平和賞';
$Hprize[7] = '災難賞';
$Hprize[8] = '超災難賞';
$Hprize[9] = '究極災難賞';
$Hprize[10]= 'いのら腕自慢';
$Hprize[11]= 'いのらコンテスト';
$Hprize[12]= 'いのらクイズ大会';

#----------------------------------------
# 外見関係
#----------------------------------------
# <BODY>タグのオプション
$htmlBody = 'BGCOLOR="#EEFFFF"';

# ゲームのタイトル文字
$Htitle = 'いのら諸島';

# タグ
# タイトル文字
$HtagTitle_ = '<FONT SIZE=7 COLOR="#8888ff">';
$H_tagTitle = '</FONT>';

# H1タグ用
$HtagHeader_ = '<FONT COLOR="#4444ff">';
$H_tagHeader = '</FONT>';

# 大きい文字
$HtagBig_ = '<FONT SIZE=6>';
$H_tagBig = '</FONT>';

# いのらの名前
$HtagIName_ = '<FONT COLOR="#4444ff"><B>';
$H_tagIName = '</B></FONT>';

# 島の名前など
$HtagName_ = '<FONT COLOR="#a06040"><B>';
$H_tagName = '</B></FONT>';

# 薄くなった島の名前
$HtagName2_ = '<FONT COLOR="#808080"><B>';
$H_tagName2 = '</B></FONT>';

# 順位の番号など
$HtagNumber_ = '<FONT COLOR="#800000"><B>';
$H_tagNumber = '</B></FONT>';

# 順位表における見だし
$HtagTH_ = '<FONT COLOR="#C00000"><B>';
$H_tagTH = '</B></FONT>';

# 開発計画の名前
$HtagComName_ = '<FONT COLOR="#d08000"><B>';
$H_tagComName = '</B></FONT>';

# 災害
$HtagDisaster_ = '<FONT COLOR="#ff0000"><B>';
$H_tagDisaster = '</B></FONT>';

# ローカル掲示板、観光者の書いた文字
$HtagLbbsSS_ = '<FONT COLOR="#0000ff"><B>';
$H_tagLbbsSS = '</B></FONT>';

# ローカル掲示板、島主の書いた文字
$HtagLbbsOW_ = '<FONT COLOR="#ff0000"><B>';
$H_tagLbbsOW = '</B></FONT>';

# ローカル掲示板、島無し観光者の書いた文字
$HtagLbbsSK_ = '<FONT COLOR="#003333"><B>';
$H_tagLbbsSK = '</B></FONT>';

# 通常の文字色(これだけでなく、BODYタグのオプションもちゃんと変更すべし
$HnormalColor = '#000000';

# 順位表、セルの属性
$HbgTitleCell   = 'BGCOLOR="#ccffcc"'; # 順位表見出し
$HbgNumberCell  = 'BGCOLOR="#ccffcc"'; # 順位表順位
$HbgNameCell	= 'BGCOLOR="#ccffff"'; # 順位表島の名前
$HbgInfoCell	= 'BGCOLOR="#ccffff"'; # 順位表島の情報
$HbgCommentCell = 'BGCOLOR="#ccffcc"'; # 順位表コメント欄
$HbgInputCell   = 'BGCOLOR="#ccffcc"'; # 開発計画フォーム
$HbgMapCell		= 'BGCOLOR="#ccffcc"'; # 開発計画地図
$HbgCommandCell = 'BGCOLOR="#ccffcc"'; # 開発計画入力済み計画

#----------------------------------------
# ヘッダー　フッター
#----------------------------------------
# ヘッダ
sub tempHeader {
	return if($Hasync);

	my($HimgFlag) = 0;
	if($HimgLine eq '' || $HimgLine eq $imageDir){
		$baseIMG = $imageDir;
		$HimgFlag = 1;
	} else {
		$baseIMG = $HimgLine;
	}
	# 画像のローカル設定のエラーを強制的に解除（文字化けじゃないです）
	$baseIMG =~ s/筑集眺餅/デスクトップ/g;

	my $time_ = get_time((stat($bbs_log))[9],1);

	out(<<END);
Content-type: text/html

<HTML>
<HEAD>
<TITLE>
$Htitle
</TITLE>
<STYLE type="text/css">
<!--
a:link		{ color:#3300CC }
a:visited	{ color:#3300CC }
a:active	{ color:#FF0000 }
a:hover	    { color:#FF0000 }
th			{ filter:blur(direction=120,strength=2) }
-->
</STYLE>
<BASE HREF="$baseIMG/">
</HEAD>
$BODY
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html">箱庭諸島スクリプト配布元</A>
　<A HREF="http://appoh.execweb.cx/hakoniwa/">箱庭Javaスクリプト版 配布元</A>
　<A HREF="http://espion.just-size.jp/archives/dist_hako/">いのら諸島スクリプト配布元</A>
　<A HREF="$toppage">トップページ</A>
　<A HREF="$bbs">$bbsname</A>$time_
　<A HREF="$HthisFile?LogFileView=1" target=_blank>最近の出来事</A>
　<A HREF="$manual">マニュアル</A>
</nobr>
<HR>
END
	if($HimgFlag) {
		out("<FONT COLOR=RED>サーバー負荷軽減の為に、画像のローカル設定を行って下さるようにお願い致します</FONT>");
		out("<HR>");
	}
}

# フッタ
sub tempFooter {
	out(<<END);
<HR>
<P align=right>
<NOBR>
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html" target=_blank>箱庭諸島スクリプト配布元</A>
　　<A HREF="$toppage">トップページ</A>
　　<A HREF="$bbs">$bbsname</A>
　　<A HREF="$HthisFile?LogFileView=1" target=_blank>最近の出来事</A>
</nobr><BR><BR>
管理者:$adminName(<A HREF="mailto:$email">$email</A>)<BR>
</P>
</BODY>
</HTML>
END

}


1;

