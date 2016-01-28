#Free L particle Brownian Motion
add a freedom to the angle of the other two particles to the central particle

#definition
##Lagrangian


##dynamic equation
$$
\begin{align}
&-m(-3\ddot{x}+l(\dot{\alpha}^2\cos{\alpha}+\dot{\beta}\cos{\beta}
+\ddot{\alpha}\sin{\alpha}+\ddot{\beta}\sin{\beta}))
= \mathbf{dB_{1x}}/dt+\mathbf{dB_{x}}+/dt\mathbf{dB_{2x}}/dt
\\
&m(3\ddot{y}+l(-\dot{\alpha}^2\sin{\alpha}-\dot{\beta}^2\sin{\beta}
+\ddot{\alpha}\cos{\alpha}+\ddot{\beta}\cos{\beta}))
= \mathbf{dB_{1y}}/dt+\mathbf{dB_{y}}+/dt\mathbf{dB_{2y}}/dt
\\
%
%
\\
&m(-\dot{x}\dot{\alpha}\cos{\alpha}-\dot{y}\dot{\alpha}\sin{\alpha}-
\ddot{x}\sin{\alpha}+\ddot{y}\cos{\alpha}+l\ddot{\alpha})
=-\sin{\alpha}\cdot\mathbf{dB_{1x}}/dt+\cos{\alpha}\cdot\mathbf{dB_{1y}}/dt
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&m(-\dot{x}\dot{\beta}\cos{\beta}-\dot{y}\dot{\beta}\sin{\beta}-
\ddot{x}\sin{\beta}+\ddot{y}\cos{\beta}+l\ddot{\beta})
=-\sin{\beta}\cdot\mathbf{dB_{1x}}/dt+\cos{\beta}\cdot\mathbf{dB_{1y}}/dt
\end{align}
$$

##Iterative Formula
####First we have

$$
\begin{align}
&3m\ddot{x}-ml\ddot{\alpha}\sin{\alpha}-ml\ddot{\beta}\sin{\beta}
=ml(\dot{\alpha}^2\cos{\alpha}+\dot{\beta}\cos{\beta})+
\mathbf{dB_{1x}}/dt+\mathbf{dB_{x}}+/dt\mathbf{dB_{2x}}/dt
\nonumber\\
&3m\ddot{y}+ml\ddot{\alpha}\cos{\alpha}+ml\ddot{\beta}\cos{\beta}
=ml(\dot{\alpha}^2\sin{\alpha}+\dot{\beta}^2\sin{\beta})+
 \mathbf{dB_{1y}}/dt+\mathbf{dB_{y}}+/dt\mathbf{dB_{2y}}/dt
\nonumber\\
%
%
\nonumber\\
&-m\ddot{x}\sin{\alpha}+m\ddot{y}\cos{\alpha}+ml\ddot{\alpha}
=m(\dot{x}\dot{\alpha}\cos{\alpha}+\dot{y}\dot{\alpha}\sin{\alpha})
-\sin{\alpha}\cdot\mathbf{dB_{1x}}/dt+\cos{\alpha}\cdot\mathbf{dB_{1y}}/dt
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\nonumber\\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&-m\ddot{x}\sin{\beta}+m\ddot{y}\cos{\beta}+ml\ddot{\beta}
=m(\dot{x}\dot{\beta}\cos{\beta}+\dot{y}\dot{\beta}\sin{\beta})-
\sin{\beta}\cdot\mathbf{dB_{1x}}/dt+\cos{\beta}\cdot\mathbf{dB_{1y}}/dt
\nonumber
\end{align}
$$

####then
$$
\begin{align}
&dx = \dot{x}dt
\nonumber\\
&(3m)d\dot{x}-(ml\sin{\alpha})d\dot{\alpha}-(ml\sin{\beta})d\dot{\beta}
=ml(\dot{\alpha}^2\cos{\alpha}+\dot{\beta}\cos{\beta})dt+
\mathbf{dB_{1x}}+\mathbf{dB_{x}}+\mathbf{dB_{2x}}
\nonumber\\
&dy = \dot{y}dt
\nonumber\\
&(3m)d\dot{y}+(ml\cos{\alpha})d\dot{\alpha}+(ml\cos{\beta})d\dot{\beta}
=ml(\dot{\alpha}^2\sin{\alpha}+\dot{\beta}^2\sin{\beta})dt+
 \mathbf{dB_{1y}}+\mathbf{dB_{y}}+\mathbf{dB_{2y}}
\nonumber\\
%
%
\nonumber\\
&(-m\sin{\alpha})d\dot{x}+(m\cos{\alpha})d\dot{y}+(ml)d\dot{\alpha}
=m(\dot{x}\dot{\alpha}\cos{\alpha}+\dot{y}\dot{\alpha}\sin{\alpha})dt
-\sin{\alpha}\cdot\mathbf{dB_{1x}}+\cos{\alpha}\cdot\mathbf{dB_{1y}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\nonumber\\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&(-m\sin{\beta})d\dot{x}+(m\cos{\beta})d\dot{y}+(ml)d\dot{\beta}
=m(\dot{x}\dot{\beta}\cos{\beta}+\dot{y}\dot{\beta}\sin{\beta})dt-
\sin{\beta}\cdot\mathbf{dB_{1x}}+\cos{\beta}\cdot\mathbf{dB_{1y}}\nonumber
\end{align}
$$

####solve this equation,we have
####velocity on x axis
$$
\begin{align}
d\dot{x}=&1/m*((\csc(\alpha)\sec(\alpha)(\cos(2\alpha)-\sin (2\beta)+\cos (2 \beta )-4)
    (2 \cos (\alpha ) (-\sin (\alpha )\mathscr{dB}_x+\nonumber\\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&3 +\sin (\alpha ) \mathscr{dB}_{2 x}\cos (\alpha )\mathscr{dB}_y+\text{dt}\cdot l m \sin (\alpha ) \omega _{\beta }^2 \cos (\beta)+
    \text{dt}\cdot l m \omega _{\alpha }^2 \sin (\alpha ) \cos (\alpha )+3\text{dt}\cdot m 
    \omega _{\alpha } \cos (\alpha ) v_x\nonumber\\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&+3 \text{dt}\cdot m \omega_{\alpha } \sin (\alpha ) v_y)-(\cos (2 \alpha )+5) (2\mathscr{dB}_y+\mathscr{dB}_{2 y}+\text{dt}\cdot l m (\omega _{\alpha }^2\cos (\alpha )+\omega _{\beta }^2 \cos (\beta )))\nonumber\\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&+(\cos (2\alpha -\beta )+5 \cos (\beta ))(-\sin (\beta ) \mathscr{dB}_x+\cos(\beta ) \mathscr{dB}_y+\text{dt}\cdot m \omega _{\beta } (\cos (\beta )
   v_x+\sin (\beta ) v_y))))\nonumber\\
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
& /\nonumber\\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
&(\sin (2 (\alpha -\beta))+\cos (2 (\alpha -\beta ))-\sin (2 \alpha )+\cos (2 \alpha )-5 \sin(2 \beta )+
    5 \cos (2 \beta )-19)+\csc (\alpha ) \sec (\alpha ) \nonumber\\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
& (2\mathscr{dB}_y+\mathscr{dB}_{2 y}+\text{dt}\cdot l m (\omega _{\alpha }^2\cos (\alpha )+
    \omega _{\beta }^2 \cos (\beta )))-\csc(\alpha ) \sec (\alpha ) \cos (\beta ) (-\sin (\beta)\mathscr{dB}_x+\cos (\beta ) \mathscr{dB}_y\nonumber\\
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
& +\text{dt}\cdot m \omega _{\beta }(\cos (\beta ) v_x+\sin (\beta )v_y))+\mathscr{dB}_x-\cot (\alpha ) \mathscr{dB}_y-\text{dt}\cdot m
   \omega _{\alpha } (\cot (\alpha ) v_x+v_y))\nonumber
\end{align}
$$

####velocity on y axis
$$
\begin{align}
d\dot{y}=&-2 ((-2 \cos (\alpha ) (-\sin (\alpha ) \text{dB}_x+\sin(\alpha ) \text{dB}_{2 x}+
    3 \cos (\alpha ) \text{dB}_y+\text{dt} l m\sin (\alpha ) \omega _{\beta }^2 \cos (\beta )+\nonumber\\
&\text{dt} l m \omega_{\alpha }^2 \sin (\alpha ) \cos (\alpha )+3 \text{dt} m \omega_{\alpha }
    \cos (\alpha ) v_x+3 \text{dt} m \omega _{\alpha } \sin(\alpha ) v_y)+(\cos (2 \alpha )+5) (2\text{dB}_y+
    \text{dB}_{2 y}+\text{dt} l m (\omega_{\alpha }^2\nonumber\\
 &\cos (\alpha )+\omega _{\beta }^2 \cos (\beta )))-(\cos (2\alpha -\beta )+5 \cos (\beta ))
    (-\sin (\beta ) \text{dB}_x+\cos(\beta ) \text{dB}_y+\text{dt} m \omega _{\beta } (\cos (\beta )
   v_x\nonumber\\
& +\sin (\beta ) v_y))))\nonumber\\
&/ \nonumber\\
&(m (\sin (2 (\alpha -\beta
   ))+\cos (2 (\alpha -\beta ))-\sin (2 \alpha )+\cos (2 \alpha )-5 \sin
   (2 \beta )+5 \cos (2 \beta )-19))\nonumber
\end{align}
$$

####velocity on $\alpha$ axis
$$
\begin{align}
\frac{1}{lm}\cdot(\sec (\alpha )\nonumber\\
&(2(\cos ^2(\beta )-\sin (\beta )\cos (\beta )-3) (2 \cos (\alpha ) (-\sin (\alpha )\text{dB}_x
    +\sin (\alpha ) \text{dB}_{2 x}+3 \cos (\alpha )\text{dB}_y+\text{dt} l m \sin (\alpha ) \omega _{\beta }^2 \cos (\beta)+\nonumber\\
&  \text{dt} l m \omega _{\alpha }^2 \sin (\alpha ) \cos (\alpha )+3\text{dt} m \omega _{\alpha } \cos (\alpha ) v_x+
    3 \text{dt} m \omega_{\alpha } \sin (\alpha ) v_y)-(\cos (2 \alpha )+5) (2\text{dB}_y+\text{dB}_{2 y}+\nonumber\\
&  \text{dt} l m (\omega _{\alpha }^2\cos (\alpha )+\omega _{\beta }^2 \cos (\beta )))+(\cos (2\alpha -\beta )+
    5 \cos (\beta )) (-\sin (\beta ) \text{dB}_x+\cos(\beta ) \text{dB}_y+\text{dt} m \omega _{\beta } (\cos (\beta )v_x+\sin (\beta ) v_y))))\nonumber\\


(\frac{}{}-\cos (\beta ) (-\sin (\beta )
   \text{dB}_x+\cos (\beta ) \text{dB}_y+\text{dt} m \omega _{\beta }
   (\cos (\beta ) v_x+\sin (\beta ) v_y))+2
   \text{dB}_y+\text{dB}_{2 y}+\text{dt} l m (\omega _{\alpha }^2
   \cos (\alpha )+\omega _{\beta }^2 \cos (\beta ))))
\end{align}
$$