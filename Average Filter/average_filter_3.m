%Moving average filter method 3%

data = csvread('Z:/EE401 Group Project/Discrete_Autocorrelated_1.csv'); %input frequency
time = data(:,1);
magnitude = data(:,2);

%creating moving average filter
window_size = 50;
t = 0;
moving_average3 = zeros(size(magnitude)); %gets size of magnitude array and fills with zeroes

%filling correct elements for each row of respective of time
%need a for loop to fill in elements
%This method didn't end up being used but still included in appendix as it furthers understanding of moving average filter

%Fill in with window_size ending on current time
for i = 1:length(magnitude)
    total = 0; %set total
    if i >= window_size %ensure greater index val is not < 0
        for j = i:i+window_size
            if j <= length(magnitude)
                total = total + magnitude(j);
            end
            if j > length(magnitude)
                total = total + magnitude((length(magnitude)));
            end
        end
        calculation = (total)/window_size;
    end
    if i < window_size
        for k = i:i+window_size %this gives the average of the data contained before the first full
            window
            total = total + magnitude(k); % correct total val
        end
        calculation = (total)/window_size; %total/(current window size)
    end
    moving_average3(i) = calculation; %sets the row val to calculation
end

figure(1)
plot(time,magnitude,'-b') %normal plot
hold on
plot(time,moving_average,'-r')
hold on
plot(time,moving_average2, '-k')
hold on
plot(time,moving_average3,'-g') %moving average filter

%Get all figure description
title('Plot of input frequency and moving average filter (lagging method)')
xlabel('Time'), ylabel('Magnitude')
legend('Input Signal','Moving Average Filter','lag+lead','Lead')
