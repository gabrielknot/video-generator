# Video Worker

**A modular, Python-based video production and rendering engine designed to automate audiovisual content creation.**

## Overview

Video Worker is an open-source project focused on developing an automated video production pipeline using Python and FFmpeg.

The project aims to simplify and automate the process of transforming multimedia assets — such as images, audio tracks, narration and subtitles — into finished videos through configurable jobs.

Rather than relying on a monolithic video editing application, Video Worker adopts a modular architecture in which each production stage can be independently developed, replaced or integrated with external services.

The long-term goal is to build a scalable video production infrastructure capable of supporting multiple content channels and different types of audiovisual content.

## Main Goals

- Automate video assembly and rendering.
- Support configuration-driven video production through JSON job definitions.
- Leverage hardware-accelerated video encoding whenever available.
- Provide a modular architecture for integrating AI-powered content generation tools.
- Support remote rendering through distributed worker machines.
- Enable multiple production pipelines and content configurations.

## Architecture

The initial architecture consists of a Python orchestration layer responsible for interpreting production jobs and coordinating FFmpeg operations.

### Core Components

| Component | Responsibility |
|---|---|
| Job Manager | Reads and validates JSON production configurations. |
| Renderer | Coordinates video composition and rendering. |
| Media Processor | Handles images, audio, video and subtitles. |
| FFmpeg Engine | Performs media processing, composition and encoding. |
| Hardware Acceleration | Uses available hardware encoders, such as Intel VAAPI. |

### Planned Integrations

The architecture is designed to accommodate additional services:

- **AI Script Generation:** Automated script creation.
- **Text-to-Speech:** Narration generation.
- **AI Image Generation:** Visual asset production.
- **Speech Recognition:** Automatic transcription and subtitle generation.
- **Video Distribution:** Integration with publishing platforms.

These integrations are planned extensions, not requirements for the initial rendering engine.

## Configuration-Driven Production

Production jobs are defined using JSON files.

Each job describes the desired output and the media assets required to generate it, including:

- Video resolution and frame rate.
- Scene sequence and duration.
- Image animation effects.
- Narration and background music.
- Subtitle configuration.
- Output destination.

This approach separates production instructions from rendering implementation.

## Technology Stack

- **Python:** Orchestration and application logic.
- **FFmpeg:** Media processing and video rendering.
- **VAAPI:** Hardware-accelerated encoding on supported Intel graphics.
- **JSON:** Job definitions and production configuration.
- **Linux:** Primary development and execution environment.

## Development Roadmap

### Phase 1 — Rendering MVP
- [ ] JSON job configuration.
- [ ] Image loading and scene composition.
- [ ] Basic camera animations (zoom and pan).
- [ ] H.264 video encoding.
- [ ] Intel VAAPI hardware acceleration.
- [ ] Audio integration.
- [ ] Subtitle rendering.

### Phase 2 — Production Automation
- [ ] Automated media asset management.
- [ ] Text-to-Speech integration.
- [ ] Automatic subtitle generation.
- [ ] AI-generated images and visual assets.
- [ ] Production templates.

### Phase 3 — Multi-Channel Management
- [ ] Multiple channel configurations.
- [ ] Independent production pipelines.
- [ ] Centralized job management.
- [ ] Production history and metadata.
- [ ] Monitoring and reporting.

### Phase 4 — Distributed Rendering
- [ ] Remote worker execution.
- [ ] Job distribution and scheduling.
- [ ] Worker resource monitoring.
- [ ] Centralized output management.
- [ ] Support for heterogeneous hardware.

## Project Status

**Early development — Rendering MVP.**

The current focus is building a reliable rendering engine capable of composing animated scenes and encoding videos using hardware acceleration.

The initial implementation targets Linux systems and Intel integrated graphics with VAAPI support.

## Design Principles

1. **Modularity:** Components should be independently replaceable.
2. **Automation:** Production should be driven by structured job definitions.
3. **Hardware Awareness:** Rendering should leverage available hardware acceleration.
4. **Extensibility:** New media processing and AI services should integrate without redesigning the core.
5. **Scalability:** The architecture should support multiple workers and production pipelines as the project evolves.

---

*Video Worker — Building the infrastructure for automated video production.*
