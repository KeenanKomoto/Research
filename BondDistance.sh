#This is a bash script that operates on a file (4x3) to compute the distances between two atoms.
#Appends those distances to a file in a main directory containing 10 sub-directories (Trial_1, Trial_2, etc.) as well as single files within each Trial directory
#Tuesday July 7, 2015
#
#
#
#
#
#
#
#
#
#
#

#Prints line in quotes into the file "Distances"
echo "Trial Snapshot BF-Distance1 BF-Distance2" > Distances

#Beginning of loops to enter sub-directories (Trial_1, Trial_2, etc) and filename/number iterations
for i in `seq 1 10`; do cd Trial_$i;
for j in `seq 20 20 3900`; do 

#Assign first variable, splitting the coordinates of Boron (B) into 3 different variables
#B1 is x coordinate, B2 is y coordinate, B3 is z coordinate
B=$(awk 'NR == 1' coordinates$j | awk '{print $2, $3, $4}');
B1=$(echo $B | cut -d' ' -f1);
B2=$(echo $B | cut -d' ' -f2);
B3=$(echo $B | cut -d' ' -f3);

#Repeat assigning variables to two Flourine (F1, F2) atoms
F1=$(awk 'NR == 2' coordinates$j | awk '{print $2, $3, $4}');
F11=$(echo $F1 | cut -d' ' -f1);
F12=$(echo $F1 | cut -d' ' -f2);
F13=$(echo $F1 | cut -d' ' -f3);

F2=$(awk 'NR == 3' coordinates$j | awk '{print $2, $3, $4}');
F21=$(echo $F2 | cut -d' ' -f1);
F22=$(echo $F2 | cut -d' ' -f2);
F23=$(echo $F2 | cut -d' ' -f3);

#Compute the distance (Dist1) between Boron (B) and Flourine (F1)
#Distance1
x1=$(echo "($F11-($B1))^2" | bc);
y1=$(echo "($F12-($B2))^2" | bc);
z1=$(echo "($F13-($B3))^2" | bc);
sum1=$(echo "$x1+$y1+$z1" | bc);
Dist1=$(echo "sqrt($sum1)" | bc);

#Compute the distance (Dist2) between Boron (B) and Flourine (F2)
#Distance2
x2=$(echo "($F21-($B1))^2" | bc);
y2=$(echo "($F22-($B2))^2" | bc);
z2=$(echo "($F23-($B3))^2" | bc);
sum2=$(echo "$x2+$y2+$z2" | bc);
Dist2=$(echo "sqrt($sum2)" | bc);

#Print out Trial number, iteration number, distance 1, and distance 2, and append it to file "Distances"
#NOTE!!!! The file "Distances" is currently located one directory back, remove the "../" in front of "Distances" if you want it to be in your current directory
echo "   $i    $j      $Dist1    $Dist2" >> ../Distances;

#Print out distance 1 and distance 2 and append to each their own file (Distance 1 goes into file "BFDistance1")
echo "$Dist1" >> BFDistance1;
echo "$Dist2" >> BFDistance2;

#End iteration loop. Move back one directory, and end sub-directory loop
done; cd ..; done
