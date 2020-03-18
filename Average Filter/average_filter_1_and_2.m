% Moving Average Filter Method 1 & 2 - Read report for methods

% Reading
data = csvread('Discrete_Autocorrelated_1.csv');

%split into separate arrays
time = data(:,1);
magnitude = data(:,2);

%creating moving average filter
window_size = 50;
t = 0;
moving_average = zeros(size(magnitude)); %gets size of magnitude array and fills with zeroes

%filling correct elements for each row of respective of time
%need a for loop to fill in elements
%Fill in with window_size ending on current time
for i = 1:length(magnitude)
    total = 0; %set total
    if i >= window_size %ensure greater index val is not < 0
        for j = (i-window_size):i
            if j >= 1
                total = total + magnitude(j);
            end
        end
        calculation = (total)/window_size;
        
    end
    if i < window_size
        for k = 1:i %this gives the average of the data contained before the first full window
            total = total + magnitude(k); % correct total val
        end
        calculation = (total)/i; %total/(current window size)
    end
    moving_average(i) = calculation; %sets the row val to calculation
end
figure(1)
plot(time,magnitude,'-b') %normal plot
hold on
plot(time,moving_average,'-g') %moving average filter

%Get all figure description
title('Plot of input frequency and moving average filter (lagging method)')
xlabel('Time'), ylabel('Magnitude')
legend('Input Signal','Moving Average Filter')
moving_average2 = zeros(size(magnitude)); %gets size of magnitude array and fills with zeroes

%Moving_average filter 2 (Centering around the current time)
%Fill in with window_size ending on current time
for i = 1:length(magnitude)
    total = 0; %set total
    if i >= window_size/2 %ensure greater index val is not < 0
        for j = (i-window_size/2):(i+window_size/2)
            if j >= 1
                if j < (length(magnitude)-window_size/2)
                    total = total + magnitude(j);
                end
            end
        end
        calculation = (total)/window_size;
    end
    if i < window_size/2
        for k = 1:i %this gives the average of the data contained before the first full window
            total = total + magnitude(k); % correct total val
        end
        calculation = (total)/i; %total/(current window size)
    end
    moving_average2(i) = calculation; %sets the row val to calculation
end

figure(2)
plot(time,magnitude,'-b') %normal plot
hold on
plot(time,moving_average,'-g') %moving average filter
hold on
plot(time,moving_average2, '-r') %second moving average filter with outputs average centered around current time

%Get all figure description
title('Plot of input frequency and moving average filter (lag+lead method)')
xlabel('Time'), ylabel('Magnitude')
legend('Input Signal','Moving Average Filter','Lag+Lead Avg Filter')

%Links to help
%https://www.gaussianwaves.com/2010/11/moving-average-filter-ma-filter-2/
%https://www.youtube.com/watch?v=7Rz_ITRIADg
