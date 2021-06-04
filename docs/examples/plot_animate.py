"""
Animate trajectories
-------------------------------
traja allows animating trajectories.
"""
import traja

df = traja.generate(1000, seed=0)

###############################################################################
# Plot a animation of trajectory
# ==============================
# An animation is generated using :func:`~traja.plotting.animate`.

anim = traja.plotting.animate(df, save=True) # saves to trajectory.mp4
anim