from affine_fit import Affine_Fit

from_pt = ((1,1),(1,2),(2,2),(2,1)) # a 1x1 rectangle
to_pt = ((4,4),(6,6),(8,4),(6,2))   # scaled x 2, rotated 45 degrees and translated

trn = Affine_Fit(from_pt, to_pt)

print "Transformation is:"
print trn.To_Str()

err = 0.0
for i in range(len(from_pt)):
    fp = from_pt[i]
    tp = to_pt[i]
    t = trn.Transform(fp)
    print ("%s => %s ~= %s" % (fp, tuple(t), tp))
    err += ((tp[0] - t[0])**2 + (tp[1] - t[1])**2)**0.5

print "Fitting error = %f" % err