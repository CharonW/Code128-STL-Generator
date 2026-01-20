UNIT = 0.6;
BAR_LENGTH = 25.0;
BAR_DEPTH = 0.5;

modules = [2, 1, 1, 2, 1, 4, 2, 2, 3, 2, 1, 1, 2, 2, 3, 1, 1, 2, 2, 2, 1, 1, 3, 2, 3, 1, 2, 1, 3, 1, 3, 1, 1, 2, 2, 2, 3, 1, 2, 1, 3, 1, 2, 3, 3, 1, 1, 1, 2];

function prefix_sum(arr, i) =
    (i <= 0) ? 0 : arr[i-1] + prefix_sum(arr, i-1);

for (i = [0 : len(modules)-1]) {
    w = modules[i] * UNIT;
    x = prefix_sum(modules, i) * UNIT;

    if (i % 2 == 0) {
        translate([x, 0, 0])
            cube([w, BAR_LENGTH, BAR_DEPTH], center=false);
    }
}
