% Copyright (c) 2015-present, Facebook, Inc.
% All rights reserved.
%
% This source code is licensed under the BSD-style license found in the
% LICENSE file in the root directory of this source tree. An additional grant 
% of patent rights can be found in the PATENTS file in the same directory.

% remove softmax from memory
for i = 1:nhops
    memory{i}.mod_query.modules(:,end) = [];
end

nepochs2 = nepochs;
lrate_decay_step2 = lrate_decay_step;
init_lrate2 = config.init_lrate;
nepochs = ls_nepochs;
nepochs = 5;%%%%%%%
lrate_decay_step = ls_lrate_decay_step;
config.init_lrate = ls_init_lrate;

datestr(now,'yyyy-mm-dd HH:MM:SS')
train;
%target_list;
save confi5;
datestr(now,'yyyy-mm-dd HH:MM:SS')
test;%%%%之前并没�?
% add softmax back
%for i = 1:nhops
%    memory{i}.mod_query.add(Softmax());
%end
nepochs = nepochs2;
lrate_decay_step = lrate_decay_step2;
config.init_lrate = init_lrate2;
train;
save confi20;
datestr(now,'yyyy-mm-dd HH:MM:SS')
test;
train;
save confi35;
datestr(now,'yyyy-mm-dd HH:MM:SS')
test;
