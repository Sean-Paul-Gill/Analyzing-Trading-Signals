% Anomaly detection

%call moving average filter
run Moving_average_filter.mlx %set this to where your moving

% start identifying mean at each point
% all things created in last file
ts_moving_average = zeros(1,length(magnitude));
%get moving average time shifted
for j = 1:length(moving_average)-window_size
    ts_moving_average(j)=moving_average(j+window_size/2);
end

%create difference matrix
difference_matrix = abs(ts_moving_average - magnitude); %essentially the error between average and original signal

% move everything to the DC line
% for ease of analysis if the signal went under DC line
dc_magnitude = magnitude+abs(min_mag);
dc_moving_average = ts_moving_average+abs(min_mag);

%Plot
figure(1)
plot(time,dc_magnitude,'b')
hold on
plot(time,dc_moving_average,'g')
hold on
plot(time, difference_matrix,'r')

%determining outliers
%must determine quartile ranges for outliers 
% mean
middle_point = transpose(zeros(1,length(magnitude)-window_size));
for j = 1:length(middle_point)
    middle_point(j)=difference_matrix(j);
end
sorted_middle_point = sort(middle_point);
median_matrix = length(sorted_middle_point)/2;
median_lower_index = floor(median_matrix);
median_upper_index = median_lower_index + 1;
median = (sorted_middle_point(median_lower_index)+sorted_middle_point(median_upper_index))/2;

%lower quartile index, upper quartile index
lower_quartile_index = floor((length(sorted_middle_point)/100)*25);
upper_quartile_index = floor((length(sorted_middle_point)/100)*75);

%lower + upper quartiles
lower_quartile = sorted_middle_point(lower_quartile_index);
upper_quartile = sorted_middle_point(upper_quartile_index);

%interquartile range
interquartile_range = upper_quartile - lower_quartile;

%lower inner fence % standard deviations are wrote here!!
lower_inner_fence = lower_quartile - 1.5*(interquartile_range);

%upper inner fence
upper_inner_fence = upper_quartile + 1.5*(interquartile_range);
%lower outer fence
lower_outer_fence = lower_quartile - 3*(interquartile_range);

%upper outer fence
upper_outer_fence = upper_quartile + 3*(interquartile_range);

mild_outlier_matrix = transpose(zeros(1,length(middle_point)));
extreme_outlier_matrix = transpose(zeros(1,length(middle_point)));

%now check data that lies outside inner fences
for i = 1:length(middle_point)
    if middle_point(i) < lower_inner_fence || middle_point(i) > upper_inner_fence
        mild_outlier_matrix(i) = middle_point(i);
    end
end

%get index values for mild outliers
mild_outlier_index_list = find(mild_outlier_matrix)
%now check data that lies outside outer fences
for i = 1:length(middle_point)
    if middle_point(i) < lower_outer_fence || middle_point(i) > upper_outer_fence
        extreme_outlier_matrix(i) = middle_point(i);
    end
end

%get index values for extreme outliers
extreme_outlier_index_list = find(extreme_outlier_matrix);

%now plot graph with the outliers
figure(2)
plot(time,magnitude,'b')
hold on
plot(time,ts_moving_average,'g')
hold on

%work out how to plot certain values
plot(time(mild_outlier_index_list),magnitude(mild_outlier_index_list),'ok')
hold on
plot(time(extreme_outlier_index_list),magnitude(extreme_outlier_index_list),'or')

%describe the plot
xlim_lower = window_size/100
xlim_upper = (length(magnitude)-window_size-1)/100
xlim([xlim_lower xlim_upper])
title('Signal vs Moving Average Filter w/ outliers marked')
xlabel('Time'), ylabel('Magnitude')
legend('Input Signal','Moving Average Filter','Mild Outlier','Extreme Outlier','Location','best')
