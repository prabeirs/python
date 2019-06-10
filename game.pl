#!/usr/bin/perl -w
use List::Util qw(shuffle);

sub fisher_yates_shuffle {
    my $deck = shift;

    my $i = @$deck;
        while ($i--) {
            my $j = int rand ($i+1);
            @$deck[$i,$j] = @$deck[$j,$i];
       }
}

sub main {
	my $numTC = 10;
	my $N = 1000; # maximum number of villains and players across 10 tests.
        my @inVl;
        my @inPl;
        my @WIN = ();
        if (scalar(@ARGV) == 2) {
            $numTC = $ARGV[0];
            $N     = $ARGV[1];
        }
        if (scalar(@ARGV) > 2) {
            print "ERROR: The first argument is no of test cases and second is max no of allowed villains and players in one test case.\n";
            print "ERROR: Otherwise if no arguments at all then default values of 10 & 1000 is fixed set respectively.\n";
            exit(2);
        }
        if (scalar(@ARGV) == 0) {
            #this is a via stdin input case. so gather the input as ordered shown in the example of the Question.
            # the first entry is  num of test rounds.
            # second is not of strengths or energies (N).
            # Third is the N strehngths of the villain(s).
            # Fourth is the N energies of the player(s).
            my @inF = ();
            while(<STDIN>) {
                my $in = $_;
                chomp $in;
                push @inF, $in;
                if (scalar(@inF) == 4) {
                    last;
                }
            }
            $numTC = $inF[0];
            $N     = $inF[1];
            @inVl  = split(" ", $inF[2]);
            @inPl  = split(" ", $inF[3]);
        }
                
	my @TC = ();
	foreach (1 .. $numTC) {
		my $random_number_participants = int(rand( $N - 1 )) + 1;
		push @TC, $random_number_participants;
	}
	foreach my $tc (@TC) {
		#print "tc = $tc\n";
		my @villain_strength = ();
		my @player_energy    = ();
                if (@inVl) {
                    @villain_strength = @inVl;
                }
                if (@inPl) {
                    @player_energy    = @inPl;
                }
                if (!scalar(@villain_strength) && !scalar(@player_energy)) {
		    foreach (1 .. $tc) {  # This $tc value is the N in question. So lets gather N strength and energy for villains and players.
			    my $random_number_strength_villain = int(rand( $tc - 1 )) + 1;
			    my $random_number_energy_player    = int(rand( $tc - 1 )) + 1;
			    #print "Vi=$random_number_strength_villain\tPl=$random_number_energy_player\n";

			    push @villain_strength, $random_number_strength_villain;
			    push @player_energy, $random_number_energy_player;

		    }
                }

		my $num_elem = $#villain_strength+1;
		my $iterate  = $num_elem;
		#print "iterate = $iterate\n";
		foreach (1 .. $iterate) {
			my $win = 0;
			my $loose =  0;
			fisher_yates_shuffle(\@villain_strength);
			fisher_yates_shuffle(\@player_energy);

			for(my $item = 0; $item <= $#player_energy; $item++) {
				if ($player_energy[$item] > $villain_strength[$item]) {
					$win++;
				} else {
					$loose++;
				}
			}

			my $winCnt = $win + 1;
			my $looseCnt = $loose + 1;
			if ($winCnt == $iterate) {
				#print "WIN\t(strength/energy=$num_elem, win=$winCnt, lose=$looseCnt)\n";
                                push @WIN, "WIN\t(strength/energy=$num_elem, win=$winCnt, lose=$looseCnt)";
			} else {
				#print "LOSE\t(strength/energy=$num_elem, win=$winCnt, lose=$looseCnt)\n";
			}

		}

		#print "==============\n";
	}
    if (@WIN) {
        print "WIN\n";
    } else {
        print "LOSE\n";
    }
}

&main;
