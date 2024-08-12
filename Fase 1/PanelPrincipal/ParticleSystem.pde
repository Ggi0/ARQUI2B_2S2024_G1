class ParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;
  float factor;
  float maxAcceleration = 0.02;
  int particleNumber;

  ParticleSystem(PVector position, float perc, int particleNum) {
    origin = position.copy();
    particleNumber = particleNum;
    factor = perc * maxAcceleration / 100; // perc -> 0 - 100, factor -> 0 - maxAcceleration
    particles = new ArrayList<Particle>();
  }

  void addParticle(float newPercentage, int widthPanelH, int posX, int posY) {
    factor = newPercentage * maxAcceleration / 100; // perc -> 0 - 100, factor -> 0 - maxAcceleration
    origin = new PVector((widthPanelH * particleNumber / 6) + posX, posY);
    particles.add(new Particle(origin, factor, maxAcceleration, widthPanelH));
  }

  void run(float nuevoPorcentHumedad, int widthPanelH, int posX, int horizontalGap) {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead() || nuevoPorcentHumedad == 0 || p.getPosition().array()[0] < posX + horizontalGap || p.getPosition().array()[0] > posX + widthPanelH - horizontalGap) {
        particles.remove(i);
      }
    }
  }
}
