% U?itaj podatke
class_counts = readtable('C:\\Users\\HP\\vestacka-i\\class_counts.csv');

% Prikaz podataka
bar(class_counts.class_type, class_counts.count)
xlabel('Tip klase')
ylabel('Broj zivotinja')
title('Broj zivotinja po tipu klase')

% Korelacija osobina
correlation_matrix = corr(table2array(data(:, 2:end-1))); % Ignorišemo prvu kolonu (animal_name) i poslednju kolonu (class_type)
figure;
heatmap(correlation_matrix, 'Colormap', pink); % Postavljamo colormap na 'pink'

% Postavljanje boje za labele
ax = gca;
ax.XColor = 'dodger blue'; % Promena boje za labele na x osi
ax.YColor = 'dodger blue'; % Promena boje za labele na y osi

% Postavljanje naslova
title('Correlation between Features');
